# Arxiv
[![Build Status](https://travis-ci.com/GarrettWilliams/Arxiv.svg?token=B2hCyDjpt2bTTR7kwpVL&branch=master)](https://travis-ci.com/GarrettWilliams/Arxiv) [![Build status](https://ci.appveyor.com/api/projects/status/no3hnrib1gnq3cbx?svg=true)](https://ci.appveyor.com/project/GarrettWilliams/arxiv)


This repository contains code for a project to automate the finding and emailing of arxiv papers on a regular schedule run on a raspberry pi. In particular the Arxiv class generates Arxiv API compatible search queries from given terms, pulls arxiv paper information, filters based on date, filters based on user created filter and can optionally directly download retrieved papers. 

Currently only the five most recent papers are grabbed - I will be updating it so that papers are chosen based on a meaningful metric and so that certain authors papers are always returned. 

## Usage
This was just a fun project to play with a raspberry pi so I won't be adding this to PyPi nor making it more robust at this time. Much of it is hard coded paths and code and so an inconvenient amount of user input is needed.

Repository is structured as follows:
* Arxiv folders contain the core code for pulling, filtering and downloading papers from Arxiv. 
* automateArxiv contains a script for generating the right folder structure before downloading, and then automatically emailing them to myself. 
* run_arxiv.sh in the root is the shell script crontab reads once a day (during weekdays). 

Should one want to use it they can clone this repository and pip install the requirements.txt folder.

Then one needs to:
<ol>
  <li> Update /automateArxiv/email_python.py paths and recipient email address. </li>
  <li> I would recommend creating a throw away email account for forwarding emails, and then storing the name and password as environment variables.</li>
  <li> Change path on run_arxiv.sh and add to crontab.</li>
  <li> If one wants different logic and papers edit the files in Arxiv/examples/query_information/*.txt and the arxiv_papers class in Arxiv.</li>
</ol>

## Examples
For a quick example of usage see the examples folder. 

## Dependencies and Framework
For the most part this is just a wrapper around a premade Python Arxiv API wrapper.

Built with:
* [arxiv](https://github.com/lukasschwab/arxiv.py)
