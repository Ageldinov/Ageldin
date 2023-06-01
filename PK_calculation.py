import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Функция третьей вкладки для расчета буферов
def PK_graph(values, window, data_file):
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

def PK_cal(values, window, data_file):
    # Исходные данные из таблицы
    df = pd.read_excel(str(data_file))

    # Дополнительные данные
    start_dose = float(values['-DOSE IN-'])  # Начальная доза (единиц концентрации)
    volume = float(values['-VOLUME IN 2-'])  # Объем ввода (единиц объема)
    start_dose_amount = values['-DOSE AMOUNT IN-'] # Размерность дозы
    volume_amount = values['-VOLUME AMOUNT IN-'] # Размерность объема
    time_units = values['-TIME IN-']  # Размерность времени
    conc_units = values['-AMOUNT IN-']  # Размерность концентрации

    # Вычисляем распределение дозы по времени
    dose = start_dose / volume  # Вычисляем концентрацию начальной дозы
    dose_amount = start_dose_amount + '/' + volume_amount # Переменная размерности концентрации
    dose_dist = dose * np.ones(len(df['Time']))  # Распределяем дозу равномерно по времени

    # Вычисляем площадь под кривой концентрации
    area = np.trapz(df['Conc'], df['Time'])

    clearence = start_dose / area

    # Вычисляем время, через которое концентрация снизится до 10% от максимальной
    max_conc = max(df['Conc'])
    ten_percent = max_conc * 0.1
    for i in range(len(df['Conc'])):
        if df['Conc'][i] < ten_percent:
            time_to_ten_percent = df['Time'][i]
            break
    for i in range(len(df['Time'])):
        if df['Time'][i] == max(df['Conc']):
            max_time = df['Time'][i]

    # Биодоступность dose reached circulation/dose administred
    f = max_conc / dose

    dist_volume = start_dose / df['Conc'][0]

    absorbed_dose = f * dose

    elemination_const = clearence / dist_volume

    half_time = 0.693 / elemination_const

    # Выводим результаты
    sg.popup((f"Дозировка, концентрация: {dose} {dose_amount}"),
            (f"Максимальная концентрация: {max_conc} {conc_units}"),
            (f"Клиренс: {round(clearence, 3)}"),
            (f'Объем распределения: {round(dist_volume, 3)}'),
            (f"Константа элюминации: {round(elemination_const, 3)}"),
            (f"Время полувыведения: {round(half_time, 3)} {time_units}"),
            (f"Площадь под кривой концентрации: {round(area, 3)} {dose_amount}*{time_units}"),
            (f"Время, через которое концентрация снизится до 10% от максимальной: {time_to_ten_percent} {time_units}"), title="Результаты расчетов")