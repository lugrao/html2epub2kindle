# Plaintext Article

A simple python script I use for converting articles to plain text and sending them to my kindle.

It relies on [txtify.it](https://txtify.it) for the text conversion.

## Setup

Store your e-mail credentials in `SENDER_ADDRESS` and `PASSWORD`.

Your Send-to-Kindle e-mail address goes in `RECEIVER_ADDRESS`.

To install the required dependencies, go to the project's root directory and type:

```
pip install -r requirements.txt
```

## Usage

Print article to the screen

```
$ python plaintext_article.py https://articles.xyz/some-article
```

Print article to the screen and save it as a `.txt` file

```
$ python plaintext_article.py https://articles.xyz/some-article -s
```

Print article to the screen, save it as a `.txt` file and send it to your kindle

```
$ python plaintext_article.py https://articles.xyz/some-article -S
```
