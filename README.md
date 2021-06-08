# DDT_Nominatim
Тестовое задание
DDT публичного API геокодинга  
Тестирование прямого и обратного геокодирования  
https://nominatim.openstreetmap.org  
  
:small_blue_diamond: Запускать test_ddt.py  
____
### main_data.py  
Создаёт список мест по случайным координатам (всего 100)  
____
### geocode.py  
Создаёт список координат, комбинируя значения одного места из главного списка, потом ищет по запросу  
Пример:  
Россия, Москва, Красная площадь  
-> Россия -> Москва -> Красная площадь -> Россия, Красная площадь -> Москва, Красная площадь -> Россия, Москва  
И так далее  
____
### info.py  
Включает в себя основные функции для тестирования  
____
### test_ddt.py  
Главный файл для прогонки тестов
