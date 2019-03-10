def is_value_valid(value):
    return isinstance(value, str) and not value == ""


def is_date_valid(date):
    return isinstance(date, str) and not date == ""
