"""
Script to pull arxiv papers and automatically email them to a recipient.

Author: Garrett Williams
Date: 2019-05-28
"""
import yagmail
import os
import sys
import datetime
from Arxiv import Arxiv

today = str(datetime.datetime.now().date())
root_folder = 'home/pi/Desktop'
path_to_papers_folder = os.path.join(root_folder, 'Arxiv_papers')
path_to_individual_date = os.path.join(path_to_papers_folder, today)

if not os.exists(path_to_folder):
    os.mkdir(path_to_folder)

if not os.exists(path_to_individual_date):
    os.mkdir(path_to_individual_date)

arxiv_today = Arxiv()
todays_papers = arxiv_today.arxiv_papers(search_string_query, store_papers=True, folder_path=path_to_individual_date)

recipients = ['williams.garrettm@gmail.com']
email_subject = f'arxiv papers from {today}'

contents = []
for arxiv_paper in os.listdir(path_to_individual_date):
    contents.append(arxiv_paper)

yagmail.SMTP(os.environ.get('automatearxiv_gmail_name'), os.environ.get('automatearxiv_gmail_password').send(to=recipients, subject=email_subject, contents=contents)
