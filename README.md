# Arxiv
[![Build Status](https://travis-ci.com/GarrettWilliams/Arxiv.svg?token=B2hCyDjpt2bTTR7kwpVL&branch=master)](https://travis-ci.com/GarrettWilliams/Arxiv) [![Build status](https://ci.appveyor.com/api/projects/status/no3hnrib1gnq3cbx?svg=true)](https://ci.appveyor.com/project/GarrettWilliams/arxiv)


This repository contains a Python class which serves as a component of a project to automate the finding and emailing of arxiv papers on a regular schedule run via a raspberry pi. In particular the Arxiv class generates Arxiv API compatible search queries from given terms, pulls arxiv paper information, filters based on date, filters based on user created filter and can optionally directly download retrieved papers. 

The current version is a quick dirty solution where the user filter just acts by taking the five most recently published papers from the last 24 hours. I will add updates in the future but this is sufficient to set up the automated portion. 

## Usage
Arxiv has not been added to PyPi yet. To use clone the repository, and then pip install the requirements.txt file. 

## Examples
For a quick example of usage see the examples folder. 

## Dependencies and Framework
For the most part this is just a wrapper around a premade Python Arxiv API wrapper.

Built with:
* [arxiv](https://github.com/lukasschwab/arxiv.py)
