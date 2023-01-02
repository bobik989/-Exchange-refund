product_money = int(input('Сколько стоит сумма всех товаров: '))
user_money = int(input('Сколько вы даете денег продавцу: '))
money = [5000, 2000, 1000, 500, 200, 100, 50, 10, 5, 2, 1]
fin_dif = []

difa = user_money - product_money
dif = difa

while dif > 0:
    for i in range(len(money)):
        while dif >= money[i]:
            dif -= money[i]
            fin_dif.append(money[i])

print(f'Ваша сдача должна составлять {difa} \nПо начилным это:')
print(*fin_dif, sep=', ')