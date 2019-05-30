import pytest
import sys
import os
path = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir))
sys.path.insert(0, path)
from Arxiv import Arxiv

def test_search_query():
    print(os.getcwd())
    authors = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), 'examples', 'query_information', 'authors.txt') 
    categories = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), 'examples', 'query_information', 'categories.txt') 
    search_query_string = Arxiv.simple_search_query_generator(authors=authors, categories=categories)
    assert len(search_query_string) > 0

def test_generate_papers():
    arxiv_example = Arxiv(number_of_repeats=2, max_results=5)
    arxiv_example._generate_papers()
    assert len(arxiv_example.queried_papers_unfiltered) > 0


def test_arxiv_papers():
    arxiv_example = Arxiv(number_of_repeats=2, max_results=5)
    search_query_string = 'au: Goodfellow OR au: McInnes OR cat: stat.ML'
    arxiv_example.arxiv_papers(search_query_string, store_papers=False)
    assert len(arxiv_example.fav_papers) > 0
 