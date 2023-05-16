# -*- coding: utf-8 -*-
"""
Naver OpenAPI Search Blog
"""

def main(search_keyword, number_search_items = 5, sort = "sim"): # sort is 'sim' or 'date'

    search_result = search_keyword + "search result of " + str(number_search_items) + " items sorted by " + sort

    return search_result
