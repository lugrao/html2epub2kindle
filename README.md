# html2epub2kindle

A python program for converting html articles to epub and sending them to your kindle.

## Setup

Store your (Gmail) e-mail credentials in `SENDER_ADDRESS` and `PASSWORD`.

Your Send-to-Kindle e-mail address goes in `RECEIVER_ADDRESS`.

To install the required dependencies, go to the project's root directory and type:

```
pip install -r requirements.txt
```

## Usage

To send an article to your kindle just execute the program in your terminal,
passing the url as an argument:

```
$ python html2epub2kindle.py https://articles.xyz/some-article
```
