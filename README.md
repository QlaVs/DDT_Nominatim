# DDT_Nominatim
Тестовое задание
DDT публичного API геокодинга

Тестирование прямого и обратного геокодирования

> main_data.py
Создаёт список мест по случайным координатам (всего 100)

> geocode.py
Создаёт список координат, комбинируя значения одного места из главного списка, потом ищет по запросу
Пример:
Россия, Москва, Красная площадь
>> Россия >> Москва >> Красная площадь >> Россия, Красная площадь >> Москва, Красная площадь >> Россия, Москва
И так далее

> info.py
Включает в себя основные функции для тестирования

> test_ddt.py
Оссновной файл для тестирования
