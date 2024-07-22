flag = True
while flag:
    znak = input('Znak kakoi?' )
    a, b = int(input('cislo1')), int(input('cislo2'))
    res = 0
    if znak == '+':
        res = a + b
    elif znak == '-':
        res = a - b
    elif znak == '*':
        res = a * b
    elif znak == '/':
        if b == 0:
            print('Деление на 0 невозможно!')
            break
        res = a / b
    print(res)
    flag = input('xocew ewe?) napecataite True ili False')