class CityError(Exception):
    pass
class NotCityError(Exception):
    pass

cities = ['Bishkek', 'Osh', 'Kara-Kol', 'Batken', 'Jalal-Abad', 'Talas', 'Naryn']

while True:
    try:
        t = int(input('''
    1. Добавить новый город
    2. Отобразить список городов
    3. Заменить город
    4. Удалить город
    5. Выход
        '''))
        print(f'Ваше действие: {t}' if t != 5 else 'Программа завершает работу.')

        if t == 1:
            city = input('Введите название города:')
            if city in cities:
                raise CityError(f'Такой город уже есть! {city} - {cities.index(city)}')
            else:
                cities.append(city)
                print('Город добавлен!')

        if t == 2:
            print('Список городов:')
            for k, i in enumerate(cities, 1):
                print(f'{k}. {i}')

        if t == 3:
            old_city = input('Текущий город: ')
            if old_city not in cities:
                raise NotCityError
            new_city = input('Новый город: ')
            if new_city in cities:
                raise CityError(f'Такой город уже есть! {new_city} - {cities.index(new_city)}')
            else:
                cities[cities.index(old_city)] = new_city
                print('Город заменен.')

        if t == 4:
            del_city = input('Введите название города: ')
            if del_city not in cities:
                raise NotCityError
            else:
                cities.remove(del_city)
                print('Город удален!')

        if t == 5:
            break

    except TypeError as err:
        print('Некорректное название!', err)
    except CityError as err:
        print(err)
    except NotCityError as err:
        print(f'Текущий город отсутствует.', err)