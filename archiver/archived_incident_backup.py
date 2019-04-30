
from json import dumps

from pymongo import ASCENDING, MongoClient

from cleaner.sanitized import ArchivedIncidentCleaner


class ArchivedIncidentBackup:
    def __init__(self):
        self.cleaner = ArchivedIncidentCleaner()
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.incidentdb
        self.archived = self.db.archived
        self.archived.create_index([('dateStarted', ASCENDING)])

    def print_entries(self, query=None):
        cursor = self.db.archived.find(query)

        for document in cursor:
            print(dumps(document, indent=4, sort_keys=False))


backup = ArchivedIncidentBackup()
backup.print_entries()
