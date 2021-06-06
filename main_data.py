"""
Создаёт список мест по случайным координатам (всего 100)
"""

import requests
import random
import json


def generate():
    url = "https://nominatim.openstreetmap.org/reverse"

    places = []
    quantity = 100

    random.seed()
    for i in range(10000):
        if quantity > 0:
            lat = (random.uniform(-85.05112878, 85.05112878))
            lon = (random.uniform(-180, 180))

            try:
                prm = {'lon': f'{lon}', 'lat': f'{lat}', 'format': 'jsonv2'}
                r = requests.get(f"{url}", params=prm)
                data = r.json()
                print(quantity, data)

                places.append({"display_name": data['display_name'], "lat": float(data['lat']),
                               "lon": float(data['lon']), "address": data['address']})
                quantity -= 1

            except:
                pass
        else:
            break

    with open("main_data.json", "w") as outfile:
        json.dump(places, outfile)


if __name__ == '__main__':
    generate()
