# подключаем библиотеки
import PySimpleGUI as sg
import random
import pandas as pd
import convertation
import buffer_calculation
import  PK_calculation
import points_coordinates

# Основная функция
def main():
        # что будет внутри окна конвертации
        convert_layout = [
                [sg.Text('Эта вкладка для конвертации размерности на основе выбранных единиц измерения.', font='Helvetica 20')],
                # затем делаем текст
                [sg.Text('Выберете исходную единицу измерения массы', font='Helvetica 20')],
                [sg.OptionMenu(values=('Пикограммы', 'Нанограммы', 'Микрограммы', 'Милиграммы'), default_value='Пикограммы',  k='-UNIT OPTION START-'),],
                [sg.Text('Выберете конечную  единицу измерения массы', font='Helvetica 20')],
                [sg.OptionMenu(values=('Пикограммы', 'Нанограммы', 'Микрограммы', 'Милиграммы'), default_value='Пикограммы',  k='-UNIT OPTION END-'),],
                [sg.Text('Введите исходное количество', font='Helvetica 20')],
                [sg.Input(key='-AMOUNT-')],
                [sg.Button('Рассчитать', enable_events=True, key='-CAlCULATE 1-', font='Helvetica 20')],
                [sg.Text('Здесь будет отображен результат', key='-RESULTS 1-', font='Helvetica 20')]
                 ]
        # что будет внутри окна расчетов буфера
        buffer_layout = [
                [sg.Text('Эта вкладка для расчета требуемой массы вещества на основе указанного объема, концентрации и названия вещества', font='Helvetica 20')],
                # затем делаем текст
                [sg.Text('Введите формулу вещества', font='Helvetica 20')],
                [sg.Input(key='-FORMULA IN-')],
                [sg.Text('Введите концентрацию в молях', font='Helvetica 20')],
                [sg.Input(key='-CONCENTRATION IN-')],
                [sg.Text('Введите объем в литрах', font='Helvetica 20')],
                [sg.Input(key='-VOLUME IN-')],
                [sg.Button('Рассчитать', enable_events=True, key='-CAlCULATE 2-', font='Helvetica 20')],
                [sg.Text('Здесь будет отображен результат', key='-RESULTS 2-', font='Helvetica 20')]
                 ]
        PK_layout = [
                [sg.Text('В данном окне вы сможете расчитать фармакокинетику и фармакодинамику', font='Helvetica 20'),
                    #sg.Button('Шпаргалка', enable_events=True, key='-HELP 1-', font='Helvetica 16')
                    ],  
                    [sg.Text('Укажите используемые величины', font='Helvetica 20')],
                    [sg.Text('Единица времени:', font='Helvetica 20'),
                     sg.OptionMenu(values=('Секунды', 'Минуты', 'Часы', 'Дни'), default_value='Часы',  k='-TIME IN-')],
                    #[sg.Text('Количество временных точек:', font='Helvetica 20'),
                    # sg.Input(key='-TIME POINTS IN-')],
                    [sg.Text('Единица концентрации:', font='Helvetica 20'),
                     sg.OptionMenu(values=('пкг/мл', 'нг/мл', 'мкг/мл', 'мг/мл'), default_value='мкг/мл',  k='-AMOUNT IN-')],
                    [sg.Text('Начальная доза:', font='Helvetica 20'),
                     sg.Input(default_text='10000', key='-DOSE IN-')],
                    [sg.Text('Единица дозы:', font='Helvetica 20'),
                     sg.OptionMenu(values=('пкг', 'нг', 'мкг', 'мг'), default_value='мкг',  k='-DOSE AMOUNT IN-')],
                    [sg.Text('Объем ввода:', font='Helvetica 20'),
                     sg.Input(default_text='1', key='-VOLUME IN 2-')],
                    [sg.Text('Единица объема:', font='Helvetica 20'),
                     sg.OptionMenu(values=('нл', 'мкл', 'мл'), default_value='мл',  k='-VOLUME AMOUNT IN-')],
                    [sg.Text('Файл с данными:', font='Helvetica 20'),
                     sg.Button('Выбрать файл', enable_events=True, key='-DATA FILE-', font='Helvetica 16')],
                    [sg.Button('Показать график', enable_events=True, key='-CALCULATE 3-', font='Helvetica 20')],
                    [sg.Button('Показать параметры', enable_events=True, key='-CALCULATE 4-', font='Helvetica 20')]   
        ]
        coordinates_layout = [
                [sg.Text('В данном окне вы сможете вычислить координаты точки(ек) на рисунке', font='Helvetica 20')],
                    [sg.Text('Укажите диапазон осей на рисунке', font='Helvetica 20')],
                    [sg.Text('Начальное значение по оси Y:', font='Helvetica 20'),
                     sg.Input(default_text='0', key='-Y START IN-'),
                     sg.Text('Конечное значение по оси Y:', font='Helvetica 20'),
                     sg.Input(key='-Y END IN-')],
                    [sg.Text('Начальное значение по оси X:', font='Helvetica 20'),
                     sg.Input(default_text='0', key='-X START IN-'),
                     sg.Text('Конечное значение по оси X:', font='Helvetica 20'),
                     sg.Input(key='-X END IN-')],
                    [sg.Text('Файл с данными:', font='Helvetica 20'),
                     sg.Button('Выбрать файл', enable_events=True, key='-OPEN PICTURE-', font='Helvetica 16')],
                    #[sg.Text('Здесь появится результат', key='-RESULT 3-', font='Helvetica 20')]  
                    ]
        dna_layout = []
        # что будет внутри окна следующего окна
        next_layout = []
        # Разметка вкладок
        layout =[[sg.TabGroup([[  sg.Tab('Массовой конвертер', convert_layout),
                                  sg.Tab('Буферный калькулятор', buffer_layout),
                                  sg.Tab('Фармакокинетика (В доработке)', PK_layout),
                                  sg.Tab('Координаты (В доработке)', coordinates_layout),
                                  sg.Tab('Праймеры (В разработке)', dna_layout),
                                  sg.Tab('В разработке', next_layout)]], key='-TAB GROUP-', expand_x=True, expand_y=True),
               ]]

        # рисуем окно, название и вкладки
        window = sg.Window('Ageldin', layout)
        # запускаем основной бесконечный цикл
        while True:
                # получаем события, произошедшие в окне
                event, values = window.read()
                # если нажали на крестик
                if event in (sg.WIN_CLOSED, 'Exit'):
                        # выходим из цикла
                        break
                # если нажали на кнопку конвертации
                if event == '-CAlCULATE 1-':
                    if str(values['-AMOUNT-']) == '':
                        sg.popup("Ошибка ввода данных")
                    else:
                        # запускаем связанную функцию
                        convertation.update(values, window)
                # если нажали на кнопку буферов
                elif event == '-CAlCULATE 2-':
                    if str(values['-FORMULA IN-']) == '' or str(values['-CONCENTRATION IN-']) == '' or str(values['-VOLUME IN-']) == '':
                        sg.popup("Ошибка ввода данных")
                    else:
                        # запускаем связанную функцию
                        buffer_calculation.buff(values, window)
                elif event == '-DATA FILE-':
                    data_file = sg.popup_get_file('Выберите файд с данными', keep_on_top=True)
                    if str(data_file) != '':
                        sg.popup("Вы выбрали: " + str(data_file), keep_on_top=True)
                elif event == '-HELP 1-':
                        sg.popup('D = Доза \nt = Интервал дозирования \nCL = Клиренс \nVd = Объем распределения \nke = Константа скорости элюминации \nka = Константа скорости абсорбции \nF = Абсорбировшаяся фракция (Биодоступность) \nK0 = Скорость инфузии \nT = Продолжительность инфузии \nC = Концентрация в плазме', font='Helvetica 14')
                elif event == '-CALCULATE 3-':
                      # запускаем связанную функцию
                    PK_calculation.PK_graph(values,window,data_file)
                elif event == '-CALCULATE 4-':
                      # запускаем связанную функцию
                    PK_calculation.PK_cal(values,window,data_file)
                elif event == '-OPEN PICTURE-':
                    if str(values['-X END IN-']) == '' or str(values['-Y END IN-']) == '':
                        sg.popup("Ошибка ввода данных")
                    else:
                        picture = sg.popup_get_file('Выберите изображение с данными', keep_on_top=True)
                        if str(picture) != '':
                            points_coordinates.coordinates(values,window,picture)

        # закрываем окно и освобождаем используемые ресурсы

        window.close()

# На случай дополнений и запуск основной функции
if __name__ == '__main__':
        main()
        convertation
        buffer_calculation
        points_coordinates
