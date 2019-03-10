import logging

from flask_restful import reqparse

from errors.api_errors import GENERIC, NOT_EXISTS_ID, EXISTS_ID, FIELD_NOT_VALID
from models.models import Entry
from resources import Resource, Response
from translators import api_translators as translator
from validators import api_validators as validator

logger = logging.getLogger(__name__)

entry_parser = reqparse.RequestParser()
entry_parser.add_argument("value", type=str)
entry_parser.add_argument("date", type=str)


class EntryHandler:
    class Entries(Resource):
        def get(self):
            response = self.repository.get_all_entries()

            return Response.success(
                [translator.entry_translator(entry) for entry in response])

        def post(self):
            args = entry_parser.parse_args()

            # Get Entry arguments
            if validator.is_value_valid(args["value"]):
                value = args["value"]
            else:
                return Response.error(FIELD_NOT_VALID)

            if validator.is_date_valid(args["date"]):
                date = args["date"]
            else:
                return Response.error(FIELD_NOT_VALID)

            entry = Entry(value=value, date=date)

            result = self.repository.add_entry(entry)

            if result:
                return Response.success({"internal_id": result})

            return Response.error(GENERIC)

    class Entry(Resource):
        def get(self, entry_id):
            response = self.repository.get_entry(entry_id)

            if response:
                return Response.success(translator.entry_translator(response))
            return Response.error(NOT_EXISTS_ID)

        def put(self, entry_id=None):
            args = entry_parser.parse_args()

            response = self.repository.get_entry(entry_id)
            if not response:
                return Response.error(NOT_EXISTS_ID)

            # Get Entry arguments
            if validator.is_value_valid(args["value"]):
                value = args["value"]
            else:
                return Response.error(FIELD_NOT_VALID)

            if validator.is_date_valid(args["date"]):
                date = args["date"]
            else:
                return Response.error(FIELD_NOT_VALID)

            entry = {
                "value": value,
                "date": date
            }

            response = self.repository.update_entry(entry_id, entry)

            if response:
                return Response.success({"internal_id": response})

            return Response.error(GENERIC)

        def delete(self, entry_id=None):
            response = self.repository.get_entry(entry_id)

            if response:
                result = self.repository.delete_entry(entry_id)
                if result:
                    return Response.success({"internal_id": result})
            return Response.error(NOT_EXISTS_ID)
