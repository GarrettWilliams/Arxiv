"""
Class for pulling and downloading arxiv papers.

Authors:
Garrett Williams
"""

import arxiv
import os
from datetime import datetime, timedelta
import re
import inspect
import time


class Arxiv():
    """
    Class for pulling and downloading Arxiv data according to some logic.

    Uses the arxiv python wrapper "arxiv" found at:
        https://github.com/lukasschwab/arxiv.py

    Parameters:
    -----------
    number_of_repeats: int, optional
        Number of times to make call to API. Due to time outs and other issues a single call 
        may fail to return all desired results.

    sort_by: string, optional
        Logic for sorting results

    max_results: int, optional
        Maximum number of results to return from an arxiv query request.

    max_chunk_results: int, optional
        Maximum number of results to return from a single request to the arxiv API.

    iterative: bool, optional
        Whether to return results or iterator over results.
    """

    def __init__(self, number_of_repeats=5, sort_by="submittedDate",
                 max_results=1000, max_chunk_results=10, iterative=True):

        args, _, _, values = inspect.getargvalues(inspect.currentframe())
        values.pop("self")

        for arg, val in values.items():
            setattr(self, arg, val)

        self.have_queried_papers = False
        self.have_query_results_filtered_date = True


    def _generate_papers(self, search_query_string=None):
        """
        Pulls information on arxiv papers including authors, summary, link, and more. Based off 
        a wrapper of the Arxiv api found here:
        """

        all_papers = []
        for _ in range(self.number_of_repeats):
            result = arxiv.query(search_query=search_query_string,
                                 sort_by=self.sort_by,
                                 max_results=self.max_results,
                                 max_chunk_results=self.max_chunk_results,
                                 iterative=self.iterative)
            for paper in result():
                all_papers.append(paper)
            time.sleep(3)

        self.queried_papers_unfiltered = list(set(all_papers))

        self.have_queried_papers = True

    def _filter_papers_time(self, search_query_string=None, date='Today'):
        """
        Takes a list of arxiv papers and filters the results by date.
        """
        
        if not self.have_queried_papers:
            self._generate_papers(search_query_string=search_query_string)

            if date == 'Today':
                today = datetime.today().replace(minute=0, second=0, hour=0,
                                                 microsecond=0) - timedelta(days=2)
                filtered = []
                for paper in self.queried_papers_unfiltered:
                    paper_publication_date = datetime.strptime(' '.join(paper['published'].split('T'))[:-1], '%Y-%m-%d %H:%M:%S')
                    if paper_publication_date >= today:
                        filtered.append(paper)
                self.query_results_filtered_date = filtered

            elif date == 'All':
                self.query_results_filtered_date = self.queried_papers_unfiltered

            else:
                filter_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                filtered = []
                for paper in self.queried_papers_unfiltered:
                    paper_publication_date = datetime.strptime(' '.join(paper['published'].split('T'))[:-1], '%Y-%m-%d %H:%M:%S')
                    if paper_publication_date >= today:
                        filtered.append(paper)
                self.query_results_filtered_date = filtered

        elif self.have_queried_papers:
            if date == 'Today':
                today = datetime.today().replace(minute=0, second=0, hour=0,
                                                 microsecond=0) - timedelta(days=2)
                filtered = []
                for paper in self.queried_papers_unfiltered:
                    paper_publication_date = datetime.strptime(' '.join(paper['published'].split('T'))[:-1], '%Y-%m-%d %H:%M:%S')
                    if paper_publication_date >= today:
                        filtered.append(paper)
                self.query_results_filtered_date = filtered

            elif date == 'All':
                self.query_results_filtered_date = self.queried_papers_unfiltered

            else:
                filter_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                filtered = []
                for paper in self.queried_papers_unfiltered:
                    paper_publication_date = datetime.strptime(' '.join(paper['published'].split('T'))[:-1], '%Y-%m-%d %H:%M:%S')
                    if paper_publication_date >= today:
                        filtered.append(paper)
                self.query_results_filtered_date = filtered

        self.have_query_results_filtered_date = True

    def arxiv_papers(self, search_query_string, papers_desired=5, date='Today', store_papers=False, file_path='default'):
        """
        Takes results of _filter_papers_time and filters down to N papers.

        Parameters:
        -----------
        search_query: str
            An arxiv compatible search query. See https://arxiv.org/help/api/user-manual#Appendices
            for information about creating queries.
            
        papers_desired: int, optional
            Number of papers to keep.
            
        date: str, optional
            Date to filter by. If 'All' does no time filtering. If not today or 'All' must be in the form '%Y-%m-%d %H:%M:%S'.

        store_papers: Bool, optional
            If true, download papers.
            
        file_path: str, optional
            File path for where to store files. 
        """
        
        self._filter_papers_time(search_query_string=search_query_string, date='Today')

        if self.have_query_results_filtered_date:
            self.fav_papers = self.query_results_filtered_date[:papers_desired]

        if store_papers:
            self._download_papers(file_path=file_path)

    def _custom_slugify(self, obj):
        """
        Function for generating arxiv paper names.
        """

        return re.sub(r'([^\s\w]|_)+', '', ' '.join(obj['title'].split()))

    def _download_papers(self, file_path):
        """
        Method for downloading retrieved papers.
        """

        if file_path == 'default':
            paper_dump = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), 'arxiv_papers')

            if not (os.path.isdir(paper_dump) and os.path.exists(paper_dump)):
                os.mkdir(paper_dump)
            for paper in self.fav_papers:
                arxiv.download(paper, dirpath=paper_dump,
                               slugify=self._custom_slugify)
        else:
            paper_dump = self.file_path

            if not (os.path.isdir(paper_dump) and os.path.exists(paper_dump)):
                os.mkdir(paper_dump)
            for paper in self.fav_papers:
                arxiv.download(paper, dirpath=paper_dump,
                               slugify=self._custom_slugify)
if __name__ == '__main__':
    example = Arxiv(number_of_repeats=2, max_results=2)
    example.arxiv_papers(papers_desired=15, store_papers=True)
