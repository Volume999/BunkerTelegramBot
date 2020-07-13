import wikipediaapi
from pprint import pprint
import re
from collections import defaultdict
import csv

class Jobs:
    names = list()
    descriptions = defaultdict(str)

    def __init__(self):
        pass


def initialize_jobs():
    jobs = Jobs()
    wiki = wikipediaapi.Wikipedia("ru")
    page_py = wiki.page("Категория:Профессии")
    # pprint(page_py.categorymembers)
    for page in page_py.categorymembers:
        pattern = r':'
        if not re.search(pattern, page):
            summary = wiki.page(page).summary
            jobs.names.append(page)
            jobs.descriptions[page] = summary
    for i in jobs.names:
        print(i)
        print(jobs.descriptions[i])
    return jobs


def main():
    jobs = initialize_jobs()


main()