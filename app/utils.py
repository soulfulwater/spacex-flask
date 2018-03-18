from datetime import datetime


def _create_date_object(date_string):
    datetime_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
    return datetime_object

