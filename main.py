product_money = int(input('Сколько стоит сумма всех товаров: '))
user_money = int(input('Сколько вы даете денег продавцу: '))
money = [1, 2, 5, 10]
fin_dif = []

difa = user_money - product_money
dif = difa
while dif > 0:

    if dif > money[3]:
        dif -= 10
        fin_dif.append(money[3])

    elif dif > money[2]:
        dif -= 5
        fin_dif.append(money[2])

    elif dif > money[1]:
        dif -= 2
        fin_dif.append(money[1])

    elif dif >= money[0]:
        dif -= 1
        fin_dif.append(money[0])
        break

print(f'Ваша сдача должна составлять {difa} \n по мелким начилным это: {fin_dif}')
