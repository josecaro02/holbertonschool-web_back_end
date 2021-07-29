#!/usr/bin/env python3
""" Task 2 hypermedia pagination"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ index range function"""
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get page method"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()

        if self.__dataset is None:
            return []

        idx_range = index_range(page, page_size)
        data = self.__dataset[idx_range[0]: idx_range[1]]
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ get hyper method"""

        data = self.get_page(page, page_size)

        data_set = self.__dataset

        if data_set:
            lenData = len(data_set)
            totPage = math.ceil(lenData / page_size)
        else:
            lenData = 0
            totPage = 0

        if not data:
            page_size = 0
        else:
            page_size = len(data)

        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        if page < totPage:
            next_page = page + 1
        else:
            next_page = None
        hyper = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': totPage
        }

        return hyper
