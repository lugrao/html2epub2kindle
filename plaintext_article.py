import requests
import sys
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# E-mail credentials
SENDER_ADDRESS = ""
PASSWORD = ""
RECEIVER_ADDRESS = ""


def main():
    usage = (
        "usage: plaintext_article.py URL [argument]\n"
        "\nPrint article to the screen.\n"
        "Optionally save it as a .txt file and send it via e-mail.\n\n"
        "positional arguments:\n"
        "    URL                  URL of the page you want the text from.\n\n"
        "optional arguments:\n"
        "    -s                   Save article as a .txt file.\n"
        "    -S                   Save article as a .txt file\n"
        "                         and send it to e-mail address."
    )

    # Validate arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit(usage)

    if len(sys.argv) == 3 and sys.argv[2] not in ["-s", "-S"]:
        sys.exit(usage)

    # Convert article to plain text via textify.it
    url = f"https://txtify.it/{sys.argv[1]}"
    user_agent = ("Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101"
                  " Firefox/89.0")

    try:
        print("Waiting response from txtify.it...\n")
        res = requests.get(url, headers={"User-Agent": user_agent})
    except requests.RequestException:
        sys.exit(1)

    # If no extra arguments, print article to screen and exit
    if len(sys.argv) == 2:
        print(res.text)
        sys.exit()

    # Save article to .txt file
    title = ""
    for char in res.text:
        if char == "\n":
            break
        elif char.isalnum() or char == " ":
            title += char

    filename = "-".join(title.lower().strip().split(' ')) + ".txt"

    with open(filename, "w") as file:
        file.write(f"{res.text}\n\n--\n{sys.argv[1]}")
        print(res.text)
        print(f"\n\n\nSaved to `{filename}`.")

    # If "-s" was passed as argument, exit
    if sys.argv[2] == "-s":
        sys.exit()

    # Send .txt file to e-mail address
    message = MIMEMultipart()
    port = 465

    print(f"Sending file to {RECEIVER_ADDRESS}...")

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment",
                    filename=("iso-8859-1", "", f"{filename}"))
    message.attach(part)
    text = message.as_string()
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(
        "smtp.gmail.com", port, context=context
    ) as server:
        server.login(SENDER_ADDRESS, PASSWORD)
        server.sendmail(SENDER_ADDRESS, RECEIVER_ADDRESS, text)
    print("Done.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exited on keyboard interrupt.")
