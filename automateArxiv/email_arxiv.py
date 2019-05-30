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
root_folder = r'C:\Users\Garrett\Desktop'
path_to_papers_folder = os.path.join(root_folder, 'Arxiv_papers')
path_to_individual_date = os.path.join(path_to_papers_folder, today)

if not os.exists(path_to_folder):
    os.mkdir(path_to_folder)

if not os.exists(path_to_individual_date):
    os.mkdir(path_to_individual_date)

arxiv_today = Arxiv()
todays_papers = arxiv_today.arxiv_papers(
    store=True, path=path_to_individual_date)

recipients = ['williams.garrettm@gmail.com']
email_subject = f'arxiv papers from {today}'
contents = []
for file in os.listdir(path):
    contents.append(file)

yagmail.SMTP().send(to=recipients, subject=email_subject, contents=contents)
