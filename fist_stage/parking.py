import random
import time

parkovka = []

text = '''
1. Получить талон
2. Проверить счет
3. Завершить счет
'''

while True:
    print(text)
    choice = input('Выбор - ')

    if choice == '1':
        nomer = input('Введите номер машины - ')
        marka = input('Введите марку машины - ')
        car = {
            'nomer': nomer,
            'marka': marka,
            'talon': random.randint(100, 999),
            'start_time': time.time()
        }
        parkovka.append(car)
        print('Машина в парковке)', car['talon'])
    elif choice == '2':
        talon = int(input('Введите талон - '))
        for i in parkovka:
            if i['talon'] == talon:
                break
        print('Машина', i['marka'], 'с номером', i['nomer'])
        print((time.time() - i['start_time']) // 60 * 5, 'сом накопилось')
    elif choice == '3':
        talon = int(input('Введите талон - '))
        for i in parkovka:
            if i['talon'] == talon:
                break
        print('Машина', i['marka'], 'с номером', i['nomer'])
        print((time.time() - i['start_time']) // 60 * 5, 'сом накопилось')
        parkovka.remove(i)
        print(parkovka)
        print('Приходите еще к нам пожалуйста')
