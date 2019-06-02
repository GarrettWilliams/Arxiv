"""
Script to pull arxiv papers and automatically email them to a recipient.

Author: Garrett Williams
Date: 2019-05-28
"""
import yagmail
import os
import sys
sys.path.insert(0, '/home/pi/Desktop/Arxiv/Arxiv')
import datetime
from Arxiv import Arxiv
import time 

today = str(datetime.datetime.now().date())
root_folder = '/home/pi/Desktop'
path_to_papers_folder = os.path.join(root_folder, 'Arxiv_papers')
path_to_individual_date = os.path.join(path_to_papers_folder, today)

if not os.path.exists(path_to_papers_folder):
    print('Creating papers root directory')
    os.mkdir(path_to_papers_folder)
    time.sleep(3)

if not os.path.exists(path_to_individual_date):
    print('Creating papers folder for today')
    os.mkdir(path_to_individual_date)

arxiv_today = Arxiv()
print('Starting to look for papers')
search_string_query  = 'au: Goodfellow OR au: McInnes OR au: Karpathy OR cat: stat.ML'
todays_papers = arxiv_today.arxiv_papers(search_string_query, store_papers=True, folder_path=path_to_individual_date, date='All')
print('We found {} papers'.format(len(arxiv_today.fav_papers)))
recipients = ['williams.garrettm@gmail.com']
email_subject = 'arxiv papers from {}'.format(today)

contents = []
for arxiv_paper in os.listdir(path_to_individual_date):
    contents.append(arxiv_paper)

yagmail.SMTP(os.environ.get('automatearxiv_gmail_name'), os.environ.get('automatearxiv_gmail_password')).send(to=recipients, subject=email_subject, contents=contents)
