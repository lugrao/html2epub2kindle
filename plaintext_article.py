import requests
import sys


usage = (
    "usage: txt.py URL [-p]\n"
    "\nPrint article to the screen. Optionally write it to a .txt file\n\n"
    "positional arguments:\n"
    "    URL                  URL of the page you want the text from.\n\n"
    "optional arguments:\n"
    "    -s                   Write article to a .txt file."
)


def main():
    if len(sys.argv) not in [2, 3]:
        sys.exit(usage)

    if len(sys.argv) == 3 and sys.argv[2] != "-s":
        sys.exit(usage)

    url = f"https://txtify.it/{sys.argv[1]}"
    user_agent = ("Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101"
                  " Firefox/89.0")

    try:
        print("Waiting response from txtify.it...\n")
        res = requests.get(url, headers={"User-Agent": user_agent})
    except requests.RequestException:
        sys.exit(1)

    title = ""
    for char in res.text:
        if char == "\n":
            break
        if char not in '<>:"\\/|?*\0':
            title += char

    filename = "-".join(title.lower().split(' ')) + ".txt"

    if len(sys.argv) == 2:
        print(res.text)
        sys.exit()

    with open(filename, "w") as file:
        file.write(f"{res.text}\n\n---\n{sys.argv[1]}")
        print(res.text)
        print(f"\n\n\nSaved to `{filename}`.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exited on keyboard interrupt.")
