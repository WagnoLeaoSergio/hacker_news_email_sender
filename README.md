# hacker_news_email_sender

[![codecov](https://codecov.io/gh/WagnoLeaoSergio/hacker_news_email_sender/branch/main/graph/badge.svg?token=HK5gZzjWS9)](https://codecov.io/gh/WagnoLeaoSergio/hacker_news_email_sender)
[![CI](https://github.com/WagnoLeaoSergio/hacker_news_email_sender/actions/workflows/main.yml/badge.svg)](https://github.com/WagnoLeaoSergio/hacker_news_email_sender/actions/workflows/main.yml)
![PyPI](https://img.shields.io/pypi/v/hacker-news-email-sender)

hacker_news_email_sender created by WagnoLeaoSergio

## Install it from PyPI

```bash
pip install hacker_news_email_sender
```

You also have to create a .env file and set the `EMAIL_PASSWORD` variable wih the properly value.

Note: If you are going to use Gmail to send the news you firstly have to go into your Google Account -> security and
enable the access for less secure apps.

## Usage

```py
from hacker_news_email_sender import News_Extractor

News_Extractor.extract_news()
News_Extractor.send_email('sender@domain.com', 'receiver@domain.com')
```

```bash
$ python -m hacker_news_email_sender sender@domain.com receiver@domain.com
#or
$ hacker_news_email_sender sender@domain.com receiver@domain.com
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
