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
day_of_the_week = datetime.datetime.now().today().weekday()
valid_days = [0,1,2,3,4]
root_folder = '/home/pi/Desktop'
path_to_papers_folder = os.path.join(root_folder, 'Arxiv_papers')
path_to_individual_date = os.path.join(path_to_papers_folder, today)

if day_of_the_week in valid_days:
    # Create root paper folder if it doesn't exist.
    if not os.path.exists(path_to_papers_folder):
        os.mkdir(path_to_papers_folder)
        time.sleep(3)

    # Create a folder for a given day.
    if not os.path.exists(path_to_individual_date):
        os.mkdir(path_to_individual_date)

    arxiv_today = Arxiv()

    # Generate search string.
    authors_path = os.path.join(root_folder, 'Arxiv', 'Arxiv', 'examples', 'query_information', 'authors.txt')
    categories_path = os.path.join(root_folder, 'Arxiv', 'Arxiv', 'examples', 'query_information', 'categories.txt')
    search_string_query = arxiv_today.simple_search_query_generator(authors=authors_path, categories=categories_path)

    todays_papers = arxiv_today.arxiv_papers(search_string_query, store_papers=True, folder_path=path_to_individual_date, date='All')

    # Define list of e-mail recipients and email subject line.
    recipients = ['williams.garrettm@gmail.com']
    email_subject = 'arxiv papers from {}'.format(today)

    contents = []
    for arxiv_paper in os.listdir(path_to_individual_date):
        contents.append(os.path.join(path_to_individual_date, arxiv_paper))

    yagmail.SMTP(os.environ.get('automatearxiv_gmail_name'), os.environ.get('automatearxiv_gmail_password')).send(to=recipients, subject=email_subject, contents=contents)
