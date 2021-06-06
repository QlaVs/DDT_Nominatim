import warnings
import requests

search_url = "https://nominatim.openstreetmap.org/search"
reverse_url = "https://nominatim.openstreetmap.org/reverse"
fmt = "jsonv2"


def get_coords(name):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        prm = {'q': f'{name}', 'format': f'{fmt}'}
        r = requests.get(f"{search_url}", params=prm)
        j = r.json()
        return float(j[0]['lat']), float(j[0]['lon'])


def get_round_coords(name):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        prm = {'q': f'{name}', 'format': f'{fmt}'}
        r = requests.get(f"{search_url}", params=prm)
        j = r.json()
        return round(float(j[0]['lat']), 3), round(float(j[0]['lon']), 3)


def get_display_name(lat, lon):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        prm = {'lon': f'{lon}', 'lat': f'{lat}', 'format': f'{fmt}'}
        r = requests.get(f"{reverse_url}", params=prm)
        j = r.json()
        return j['display_name']
