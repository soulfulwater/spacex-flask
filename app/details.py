import requests


def get_launch_details(id):
    r = requests.get('https://api.spacexdata.com/v2/launches?flight_number=%d' % id)
    if r.status_code == 200:
        data = r.json()
        return data[0]
    else:
        return 'error'