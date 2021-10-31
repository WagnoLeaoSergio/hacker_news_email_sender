import argparse  # pragma: no cover
from . import newsExctractor


def main() -> None:  # pragma: no cover
    """
    The main function executes on commands:
    `python -m hacker_news_email_sender` and `$ hacker_news_email_sender `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """


    extractor = newsExctractor.News_extractor()
    extractor.extract_news()
    extractor.send_email()


if __name__ == "__main__":  # pragma: no cover
    main()
