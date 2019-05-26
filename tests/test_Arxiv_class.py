import pytest
import sys
import os
path = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), 'arxiv')
sys.path.insert(0, path)
from Arxiv import Arxiv

Arxiv = Arxiv(number_of_repeats=2, max_results=5)

# Test search_query_string
Arxiv._search_query()
assert len(Arxiv.search_query_string) > 0

Arxiv._generate_papers()
assert len(Arxiv.queried_papers_unfiltered) > 0

Arxiv.arxiv_papers(store_papers=False)
assert (len(Arxiv.fav_papers))