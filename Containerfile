FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
CMD ["hacker_news_email_sender"]
