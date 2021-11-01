import argparse
from . import newsExctractor


def main() -> None:  # pragma: no cover
    """
    The main function executes on commands:
    `python -m hacker_news_email_sender` and `$ hacker_news_email_sender `.

    The program's entry point.
    """

    parser = argparse.ArgumentParser(
        description='Extract and send the Hacker News to an email.'
    )
    parser.add_argument(
        "sender",
        type=str,
        help='The email address used to send the email'
    )

    parser.add_argument(
        "receiver",
        type=str,
        help='The email address that will receive the news.'
    )
    args = parser.parse_args()

    if args.sender and args.receiver:
        extractor = newsExctractor.News_extractor()
        extractor.extract_news()
        extractor.send_email(args.sender, args.receiver)


if __name__ == "__main__":  # pragma: no cover
    main()
