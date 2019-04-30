"""
This module does blah.
"""

from datetime import datetime
from json import dumps
# from random import randint
from re import split, sub

from cleaner import lowercase_list
from scraper.archived import ArchivedIncidentScraper


class ArchivedIncidentCleaner:
    def __init__(self):
        self.scraper = ArchivedIncidentScraper()

    # noinspection PyMethodMayBeStatic
    def line_after(self, identifier, lines):
        try:
            return lines[lines.index(identifier) + 1]
        except ValueError:
            return None

    def reformat_incident(self, archive_year, page_number):
        incident = self.reformat_incidents(archive_year, page_number, 1)[0]

        return incident

    def reformat_incidents(self, archive_year, page_number, page_size):
        incidents = self.scraper.incidents(archive_year, page_number, page_size)
        reformatted = []

        for incident in incidents:
            lines = split(r'\n+|\s\s+', incident.text.strip())

            json_data = {
                'name': self.line_after('Name:', lines),
                'county': self.line_after('County:', lines),
                'location': self.line_after('Location:', lines),
                'unit': self.line_after('Administrative Unit:', lines),
                'notes': self.line_after('Status/Notes:', lines),
                'dateStarted': self.line_after('Date Started:', lines),
                'lastUpdated': self.line_after('Last update:', lines)
            }

            reformatted.append(json_data)

        return reformatted

    def clean_incidents(self, archive_year, page_number, page_size):
        incidents = self.reformat_incidents(archive_year, page_number, page_size)
        cleaned = []

        for uncleaned_incident in incidents:
            incident = {}

            #
            name = uncleaned_incident.get('name')
            incident.__setitem__('name', name)

            #
            counties = split(r', +| +/ +', sub(r' +\b(County)\b', '',
                                               uncleaned_incident.get('county')))
            incident.__setitem__('counties', counties)

            #
            location = uncleaned_incident.get('location').capitalize().strip().split()
            for word in location:
                if word not in lowercase_list:
                    location[location.index(word)] = word.title()
            location = ' '.join(location)
            incident.__setitem__('location', location)

            #
            units = split(r', +| *\/ *', sub(r' +\b(Unit)\b| +\b(and)\b', '',
                                             uncleaned_incident.get('unit')))
            incident.__setitem__('units', units)

            #
            notes = split(r' *- *| *\*+ *', uncleaned_incident.get('notes'))
            if '' is notes[0]:
                notes = None
            incident.__setitem__('notes', notes)

            #
            date_started = dumps(datetime.strptime(uncleaned_incident.get('dateStarted'),
                                                   '%B %d, %Y %I:%M %p'), default=str).strip('"')
            incident.__setitem__('dateStarted', date_started)

            cleaned.insert(0, incident)

        # print(dumps(cleaned, indent=4, sort_keys=False))

        return cleaned

    def clean_all_incidents(self):
        cleaned = []

        for year in range(2003, 2018):
            for incident in self.clean_incidents(year, 1, 'all'):
                cleaned.append(incident)

        # print(dumps(cleaned, indent=4, sort_keys=False))

        return cleaned


__cleaner__ = ArchivedIncidentCleaner()
__cleaner__.clean_all_incidents()
