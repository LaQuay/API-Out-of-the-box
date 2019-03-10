# -*- coding: utf-8 -*-
from core import database


class ApiRepository:
    def add_entry(self, entry):
        return database.add_entry(entry)

    def get_all_entries(self):
        return database.get_all_entries()

    def get_entry(self, entry_id):
        return database.get_entry(entry_id)

    def update_entry(self, entry_id, entry):
        return database.update_entry(entry_id, entry)

    def delete_entry(self, entry_id):
        return database.delete_entry(entry_id)
