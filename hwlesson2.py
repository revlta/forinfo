#hw 1
a = float(input())
b = float(input())
if b == 0:
    print('ты на ноль делишь дурак')
else:
    print(a / b)
#hw 2
summa = int(input())
if summa > 20:
    print(f'стоимость составила {round(summa - (summa * 0.35), 2)}, ваша скидка 35%')
else:
    print('денег мало скидки нет ха')
#hw 3
a = int(input())
m = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
if 1 <= a <= 12:
    if 9 <= a < 12:
        print(f'это {m[a]}, осень')
    elif 3 <= a < 6:
        print(f'это {m[a]}, весна')
    elif 6 <= a < 9:
        print(f'это {m[a]}, лето')
    else:
        print(f'это {m[a]}, зима')
else:
    print('такого месяца нет(')