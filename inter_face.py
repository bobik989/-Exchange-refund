from tkinter import *

win = Tk()
win.title('Сдача')
win.geometry('800x600')
win.resizable(True, False)

dif = 0
fin_dif = []
money = [1, 2, 5, 10, 50, 100, 200, 500, 1000, 2000, 5000]

def fun():
    fin_dif = []
    user = int(user_money.get())
    product = int(products_money.get())
    dif =  product - user #хз почему так
    txt3.configure(text= f'Ваша сдача должна быть: {dif}')
    while dif > 0:
        if dif >= money[10]:
            dif -= 5000
            fin_dif.append(money[10])

        elif dif >= money[9]:
            dif -= 2000
            fin_dif.append(money[9])

        elif dif >= money[8]:
            dif -= 1000
            fin_dif.append(money[8])

        elif dif >= money[7]:
            dif -= 500
            fin_dif.append(money[7])

        elif dif >= money[6]:
            dif -= 200
            fin_dif.append(money[6])

        elif dif >= money[5]:
            dif -= 100
            fin_dif.append(money[5])

        elif dif >= money[4]:
            dif -= 50
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

    txt4.configure(text= f'По наличным это: {fin_dif}')

def null():
    user_money.delete(0, END)
    products_money.delete(0, END)
    txt3.configure(text='Ваша сдача должна быть:')
    txt4.configure(text='По наличным это:')

txt1 = Label(win, text='Сумма всех продуктов:', font='Calibri 20')
txt1.place(x=40, y=50)

txt2 = Label(win, text='Сколько вы отдали денег:', font='Calibri 20')
txt2.place(x=10, y=150)

user_money = Entry(win, font='Calibri 30')
user_money.place(x=330, y=50)

products_money = Entry(win, font='Calibri 30')
products_money.place(x=330, y=150)

btn = Button(win, text='Расчитать', font='Calibri 20', command=fun)
btn.place(x=400, y=230)

btn1 = Button(win, text='Сброс', font='Calibri 20', command=null)
btn1.place(x=550, y=230)

txt3 = Label(win, text='Ваша сдача должна быть:', font='Calibri 20')
txt3.place(x=40, y=350)

txt4 = Label(win, text='По наличным это:', font='Calibri 20')
txt4.place(x=40, y=400)

win.mainloop()
