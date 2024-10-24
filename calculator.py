from tkinter import *
import tkinter.messagebox as mb

class Kalc():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def summa(self):
        return self.a + self.b

    def vichitaniye(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def div(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return "Деление на ноль невозможно"

class Ppamoyg():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perim(self):
        if self.a > 0 and self.b > 0:
            return (self.a + self.b) * 2
        return 0

    def ploshad(self):
        if self.a > 0 and self.b > 0:
            return self.a * self.b
        return 0

root = Tk()
root.title("Калькулятор")
root.geometry('600x600')

# функции для выходов из окон
def exit_off_root():
    root.destroy()

def replace_in_kalc_root():
    global tb1, tb2
    arg1 = tb1.get()
    arg2 = tb2.get()
    tb1.delete(0, END)
    tb1.insert(0, arg2)
    tb2.delete(0, END)
    tb2.insert(0, arg1)

def clean_in_kalc_root():
    global tb1, tb2
    tb1.delete(0, END)
    tb2.delete(0, END)

def show():
    massage = ("Это приложение суперское для подсчета суммы, разности, произведения и частного. "
               "Также оно умеет считать площадь и периметр и выводить прямоугольник)")
    mb.showinfo("Справка", massage)

mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu1 = Menu(mainmenu, tearoff=0)
filemenu1.add_command(label="Выход", command=exit_off_root)

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Очистить данные", command=clean_in_kalc_root)

mainmenu.add_cascade(label="Файл", menu=filemenu1)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

def func_C():
    global kalc_root, tb1, tb2, label_result
    kalc_root = Toplevel(root)
    kalc_root.title("Калькулятор")
    kalc_root.geometry('600x600')

    def calculate(operation):
        try:
            num1 = int(tb1.get())
            num2 = int(tb2.get())
            a = Kalc(num1, num2)
            if operation == '+':
                result = a.summa()
            elif operation == '-':
                result = a.vichitaniye()
            elif operation == '*':
                result = a.multiply()
            elif operation == '/':
                result = a.div()
            res1 = f'Ans: {num1} {operation} {num2} = {result}'
            label_result.config(text=res1)
        except ValueError:
            label_result.config(text="Ошибка: введите целые числа!")

    label1 = Label(kalc_root, text="Первое число")
    label1.pack()
    tb1 = Entry(kalc_root)
    tb1.pack()
    label2 = Label(kalc_root, text="Второе число")
    label2.pack()
    tb2 = Entry(kalc_root)
    tb2.pack()

    button_sum = Button(kalc_root, text="+", command=lambda: calculate('+'))
    button_sum.pack()
    button_sub = Button(kalc_root, text="-", command=lambda: calculate('-'))
    button_sub.pack()
    button_mult = Button(kalc_root, text="*", command=lambda: calculate('*'))
    button_mult.pack()
    button_div = Button(kalc_root, text="/", command=lambda: calculate('/'))
    button_div.pack()

    label_result = Label(kalc_root, text="")
    label_result.pack()

    clean_button = Button(kalc_root, text="Очистить форму", command=clean_in_kalc_root)
    clean_button.pack()

    swap_button = Button(kalc_root, text="Поменять местами аргументы", command=replace_in_kalc_root)
    swap_button.pack()

def func_P():
    global pramoyg_root, tb11, tb22, label_result
    pramoyg_root = Toplevel(root)
    pramoyg_root.title("Прямоугольник")
    pramoyg_root.geometry('600x600')

    def calculate_pramoyg(operation):
        try:
            num1 = int(tb11.get())
            num2 = int(tb22.get())
            x = Ppamoyg(num1, num2)
            if operation == 'perimeter':
                result = x.perim()
                res1 = f'Периметр: {result}'
            elif operation == 'area':
                result = x.ploshad()
                res1 = f'Площадь: {result}'
            label_result.config(text=res1)
        except ValueError:
            label_result.config(text="Ошибка: введите целые числа!")

    label1 = Label(pramoyg_root, text="Введите высоту ")
    label1.pack()
    tb11 = Entry(pramoyg_root)
    tb11.pack()
    label2 = Label(pramoyg_root, text="Введите длину ")
    label2.pack()
    tb22 = Entry(pramoyg_root)
    tb22.pack()

    button_perimeter = Button(pramoyg_root, text="Периметр", command=lambda: calculate_pramoyg('perimeter'))
    button_perimeter.pack()
    button_area = Button(pramoyg_root, text="Площадь", command=lambda: calculate_pramoyg('area'))
    button_area.pack()

    label_result = Label(pramoyg_root, text="")
    label_result.pack()

# Главное окно для выбора между калькулятором и прямоугольником
var = IntVar()
var.set(0)
Radiobutton(root, text="Калькулятор", command=func_C, variable=var, value=0).place(x=20, y=0, width=100, height=25)
Radiobutton(root, text="Прямоугольник", command=func_P, variable=var, value=1).place(x=20, y=20, width=100, height=25)

root.mainloop()
