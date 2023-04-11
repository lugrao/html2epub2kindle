# html2epub2kindle

A python program for converting html articles to epub and sending them to your kindle.

## Setup

Clone the repository and go to its directory:

```
$ git clone https://github.com/lugrao/html2epub2kindle.git
$ cd html2epub2kindle
```

Create a `.env` file and store your **Gmail** and **kindle** credentials:

```
$ echo 'SENDER_ADDRESS=<your_Gmail_address>
PASSWORD=<your_Google_App_Password>
RECEIVER_ADDRESS=<your_send_to_kindle_address>' > .env
```

Create a virtual environment:

```
$ python -m venv /path/to/new/virtual/environment
```

Activate the virtual environment:

```
$ source /path/to/new/virtual/environment/bin/activate
```

Install the required dependencies:

```
$ python -m pip install -r requirements.txt
```

## Usage

To send an article to your kindle just execute the program in your terminal,
passing the url as an argument:

```
$ python html2epub2kindle.py https://articles.xyz/some-article
```
