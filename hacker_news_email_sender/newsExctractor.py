import requests
import smtplib
import datetime
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class News_extractor:
    def __init__(self) -> None:
        self.current_time = datetime.datetime.now()
        self.content = ''

    def extract_news(self, url: str='https://news.ycombinator.com/') -> str:
        '''
        Scraps the Hacker News WebSite and creates a
        HTML string with the titles of the newest news.

        Arguments
        ---------
        url (str): URL of the WebSite.

        Return
        --------
        extracted_content (str): HTML string with a list of titles.
        '''
        print('Extracting Hacker News Stories...')
        extracted_content = ''
        extracted_content += ('<b>HN Top Stories: </b>\n'+'-'*50+'<br>')

        response = requests.get(url)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        for i, tag in enumerate(soup.find_all(
            'td',
            attrs={'class': 'title', 'valign': ''}
        )):
            if tag.text != 'More':
                extracted_content += ((str(i+1) + ' :: ' + tag.text + "\n" + '<br>'))
            else:
                extracted_content += ''

        self.content += extracted_content
        self.content += ('<br>-------------<br>')
        self.content += ('<br><br>End of Message')

        return self.content
