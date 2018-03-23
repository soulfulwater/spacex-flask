import requests

from app.utils import _create_date_object


def get_launches(return_all=False):
    r = requests.get('https://api.spacexdata.com/v2/launches')
    if r.status_code == 200:
        data = r.json()
        data.reverse()
        if not return_all:
            data = data[:3]
        spacex_launches = []
        for item in data:
            date = _create_date_object(item['launch_date_utc'])
            launch_dict = {
                'flight_number': item['flight_number'],
                'launch_date': date,
                'rocket': item['rocket']['rocket_name'],
                'successful': item['launch_success'],
                'mission_patch': item['links']['mission_patch'],
            }
            spacex_launches.append(launch_dict)
        return spacex_launches
    else:
        return 'error'
