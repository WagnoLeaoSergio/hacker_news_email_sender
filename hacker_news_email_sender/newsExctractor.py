import os
import requests
import smtplib
import datetime
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class News_extractor:
    def __init__(self) -> None:
        self.current_time = datetime.datetime.now()
        self.content = ''
        self.SERVER = 'smtp.gmail.com'
        self.PORT = 587

    def extract_news(self, url: str = 'https://news.ycombinator.com/') -> str:
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
                extracted_content += str(i+1)
                extracted_content += ' :: '
                extracted_content += tag.text + "\n" + '<br>'
            else:
                extracted_content += ''

        self.content += extracted_content
        self.content += ('<br>-------------<br>')
        self.content += ('<br><br>End of Message')

        return self.content

    def send_email(self, from_: str, to_: str) -> None:
        '''
        Sends the email with the extracted news to someone's email.

        Arguments
        ---------

        Return
        --------
        '''
        load_dotenv()
        pass_ = str(os.getenv('EMAIL_PASSWORD'))

        message = MIMEMultipart()
        message['Subject'] = 'Top News Stories HN [Automated Email]'
        message['Subject'] += ' '
        message['Subject'] += str(self.current_time.day) + \
            '-' + str(self.current_time.year)

        message['From'] = from_
        message['To'] = to_
        message.attach(MIMEText(self.content, 'html'))

        print('Initiating server...')

        server = smtplib.SMTP(self.SERVER, self.PORT)
        server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.login(from_, pass_)
        server.sendmail(from_, to_, message.as_string())

        print('Email sent...')

        server.quit()
        return
