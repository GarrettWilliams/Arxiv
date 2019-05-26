# Arxiv
[![Build Status](https://travis-ci.com/GarrettWilliams/Arxiv.svg?token=B2hCyDjpt2bTTR7kwpVL&branch=master)](https://travis-ci.com/GarrettWilliams/Arxiv)

Arxiv class for generating and storing arxiv papers. 

Currently this class is used to create an arxiv API compatible search query, generate papers from that search query,
filter based on date and a user defined filter (to be implemented) and then the results are downloaded locally.

This is a quick and dirty solution as part of a larger project to automatically pull arxiv papers and e-mail them to myself (as part of a learning project to learn how raspberry pis work), so I don't know if I will be adding more to this repository.

## Usage
To be added...

A search query is generated from three files: authors.txt, key_phrases.txt and categories.txt. Authors.txt contains a list of authors to search for, key_phrases.txt contains phrases to search for (e.g., machine learning, natural language processing) and categories are Arxiv category labels. The search query then combined all terms in all categories via logical ORs.

## Examples

## Dependencies and Framework
This class uses a premade Python Arxiv API wrapper.

Built with:
* [arxiv](https://github.com/lukasschwab/arxiv.py)
