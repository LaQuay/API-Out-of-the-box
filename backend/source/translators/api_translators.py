# -*- coding: utf-8 -*-


def entry_translator(entry_from_db):
    return {
        "id": entry_from_db.id,
        "value": entry_from_db.value,
        "date": entry_from_db.date,
    }
