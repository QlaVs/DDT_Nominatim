"""
Создаёт список координат, комбинируя значения одного места из главного списка, потом ищет по запросу
Пример:
Россия, Москва, Красная площадь
>> Россия >> Москва >> Красная площадь >> Россия, Красная площадь >> Москва, Красная площадь >> Россия, Москва
И так далее
"""

import json
import pandas
import info
import itertools
import requests


def geocoding():

    places = []
    quantity = 100

    url = info.search_url

    data = pandas.read_json('main_data.json')
    for i in range(len(data.index)):
        names = data.loc[i]['display_name'].split(',')
        for j in range(1, len(names) + 1):
            for name in itertools.combinations(names, j):
                if quantity >= 0:

                    try:
                        format_name = ','.join(name).replace(' ', '+')
                        if format_name[0] == "+":
                            format_name = format_name[1:]
                        print(quantity, format_name.replace('+', ' '))
                        r = requests.get(f"{url}?q={format_name}&format=jsonv2")
                        json_data = r.json()
                        for z in json_data:
                            places.append({"name": format_name.replace('+', ' '),
                                           'display_name': z['display_name'],
                                           'lat': float(z['lat']),
                                           'lon': float(z['lon'])})

                        # Выглядит лучше, но усложняет тест
                        # places.append({
                        #     "name": f"{name_str}",
                        #     "info": [{'display_name': z['display_name'],
                        #               'lat': float(z['lat']),
                        #               'lon': float(z['lon'])} for z in json_data]
                        # })

                        quantity -= 1

                    except:
                        pass

    with open("geocode.json", "w") as outfile:
        json.dump(places, outfile)


if __name__ == '__main__':
    geocoding()
