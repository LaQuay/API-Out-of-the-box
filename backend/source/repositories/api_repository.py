# -*- coding: utf-8 -*-
from core import database


class ApiRepository:
    @staticmethod
    def add_entry(entry):
        return database.add_entry(entry)

    @staticmethod
    def get_all_entries():
        return database.get_all_entries()

    @staticmethod
    def get_entry(entry_id):
        return database.get_entry(entry_id)

    @staticmethod
    def update_entry(entry_id, entry):
        return database.update_entry(entry_id, entry)

    @staticmethod
    def delete_entry(entry_id):
        return database.delete_entry(entry_id)
