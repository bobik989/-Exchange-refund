product_money = int(input('Сколько стоит сумма всех товаров: '))
user_money = int(input('Сколько вы даете денег продавцу: '))
money = [1, 2, 5, 10, 100, 200, 500, 1000, 2000, 5000]
fin_dif = []

difa = user_money - product_money
dif = difa
while dif > 0:
    if dif >= money[9]:
        dif -= 5000
        fin_dif.append(money[9])

    elif dif >= money[8]:
        dif -= 2000
        fin_dif.append(money[8])

    elif dif >= money[7]:
        dif -= 1000
        fin_dif.append(money[7])

    elif dif >= money[6]:
        dif -= 500
        fin_dif.append(money[6])

    elif dif >= money[5]:
        dif -= 200
        fin_dif.append(money[5])

    elif dif >= money[4]:
        dif -= 100
        fin_dif.append(money[4])

    elif dif >= money[3]:
        dif -= 10
        fin_dif.append(money[3])

    elif dif >= money[2]:
        dif -= 5
        fin_dif.append(money[2])

    elif dif >= money[1]:
        dif -= 2
        fin_dif.append(money[1])
        
    elif dif >= money[0]:
        dif -= 1
        fin_dif.append(money[0])
        break

print(f'Ваша сдача должна составлять {difa} \nПо начилным это:')
print(*fin_dif, sep=', ')
