import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt


#Функция третьей вкладки для расчета буферов
def PK_cal(values, window, data_file):
    df = pd.read_excel(str(data_file))
    # создаем график
    plt.plot(df['Time'], df['Conc'])

    # добавляем название осей
    time = values['-TIME IN-']
    amount = values['-AMOUNT IN-']

    plt.xlabel(f'Время, {time}')
    plt.ylabel(f'Концентрация, {amount}')

    # показываем график
    graph = plt.show()
    