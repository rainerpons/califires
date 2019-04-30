
# from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup
# import pandas as pd


# Uses BeautifulSoup to scrape the CAL FIRE archived incidents webpage
class ArchivedIncidentScraper:
    # noinspection PyMethodMayBeStatic
    def incidents(self, archive_year, page_number, page_size):
        base_url = 'http://cdfdata.fire.ca.gov/incidents/incidents_archived'
        full_url = base_url + '?archive_year={}&pc={}&cp={}'.format(archive_year, page_size, page_number)

        bs = BeautifulSoup(urlopen(full_url), features='html.parser')
        tables = bs.findAll('table', {
            'class': 'incident_table',
            'title': (lambda t: t != 'Search for an incident')
        })

        return tables

    def incidents_from_year(self, archive_year):
        tables = reversed(self.incidents(archive_year, 1, 'all'))
        return tables

    def all_incidents(self):
        tables = self.incidents(2013, 1, 'all')

        for year in range(2014, 2018):
            tables.append(self.incidents(year, 1, 'all'))

        return tables

    def print_incidents_from_year(self, archive_year):
        for table in self.incidents_from_year(archive_year):
            print(table.text)

    def print_all_incidents(self):
        for year in range(2013, 2018):
            self.print_incidents_from_year(year)
