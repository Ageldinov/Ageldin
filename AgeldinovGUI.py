# подключаем библиотеки
import PySimpleGUI as sg
import random
from molmass import Formula

# Основная функция
def main():
        #Функция второй вкладки для расчета буферов
        def buff():
                # Переменные
                Chem = Formula(values['-ChemIN-'])
                Vol = values['-SizeIN-']    
                Conc = values['-ConcIN-']
                # Рассчет
                Conc2 = float(Chem.mass) * float(Vol) * float(Conc)
                # Находим текст вывода и выводим в него все данные и результат
                text_elem = window['-text2-']
                text_elem.update("Для получения {} с концентрацией {} M. в объеме {} л. необходимо взять {} г.".format(Chem, Conc, Vol, round(Conc2, ndigits=3)))

        # Функция первой вкладки для конвертации величин
        def update():        
                # Задаем дефолтные значения
                num = values['-IN-']
                r = 1
                # Считываем значения с вкладки
                s1 = values['-OPTION MENU-']
                s2 = values['-OPTION MENU 2-']
                if s1 == 'Пикограммы':
                        s1 = 'пкг.'
                        if s2 == "Пикограммы":
                                s2 = 'пкг.'
                        elif s2 == "Нанограммы":
                                r = 0.001
                                s2 = 'нг.'
                        elif s2 == "Микрограммы":
                                r = 0.000001
                                s2 = 'мкг.'
                        elif s2 == "Милиграммы":
                                r = 0.000000001
                                s2 = 'мг.'                  
                elif s1 == 'Нанограммы':
                        s1 = 'нг.'
                        if s2 == "Пикограммы":
                                r = 1000
                                s2 = 'пкг.'
                        elif s2 == "Нанограммы":
                                s2 = 'нг.'
                        elif s2 == "Микрограммы":
                                r = 0.001
                                s2 = 'мкг.'
                        elif s2 == "Милиграммы":
                                r = 0.000001
                                s2 = 'мг.'  
                elif s1 == 'Микрограммы':
                        s1 = 'мкг.'
                        if s2 == "Пикограммы":
                                r = 1000000
                                s2 = 'пкг.'
                        elif s2 == "Нанограммы":
                                r = 1000
                                s2 = 'нг.'
                        elif s2 == "Микрограммы":
                                s2 = 'мкг.'
                        elif s2 == "Милиграммы":
                                r = 0.001
                                s2 = 'мг.'  
                elif s1 == 'Милиграммы':
                        s1 = 'мг.'
                        if s2 == "Пикограммы":
                                r = 1000000000
                                s2 = 'пкг.'
                        elif s2 == "Нанограммы":
                                r = 1000000
                                s2 = 'нг.'
                        elif s2 == "Микрограммы":
                                r = 1000
                                s2 = 'мкг.'
                        elif s2 == "Милиграммы":
                                s2 = 'мг.'
                # Нужно доработать ошибки ввода данных
                else:
                        text_elem.update("Ошибка ввода данных")
                # Расчеты и вывод результатов
                r2 = r * float(num)
                # получаем доступ к текстовому элементу
                text_elem = window['-text-']
                # выводим в него текст с новым числом
                text_elem.update("Результат: {} {} это {} {}".format(num, s1, round(r2, ndigits=9), s2))
        
        # что будет внутри окна конвертации
        convert_layout = [
                [sg.Text('В данном окне при выборе размерностей и вводе значения отобразится искомая размерность', font='Helvetica 20')],
                # затем делаем текст
                [sg.Text('Выберете исходную размерность', font='Helvetica 20')],
                [sg.OptionMenu(values=('Пикограммы', 'Нанограммы', 'Микрограммы', 'Милиграммы'), default_value='Пикограммы',  k='-OPTION MENU-'),],
                [sg.Text('Выберете конечную размерность', font='Helvetica 20')],
                [sg.OptionMenu(values=('Пикограммы', 'Нанограммы', 'Микрограммы', 'Милиграммы'), default_value='Пикограммы',  k='-OPTION MENU 2-'),],
                [sg.Text('Введите исходную величину', font='Helvetica 20')],
                [sg.Input(key='-IN-')],
                [sg.Button('Посчитать', enable_events=True, key='-FUNCTION-', font='Helvetica 16', visible='Жмякни меня и случится чудо')],
                [sg.Text('Здесь появится результат', key='-text-', font='Helvetica 20')]
                 ]
        # что будет внутри окна расчетов буфера
        buffer_layout = [
                [sg.Text('В данном окне при вводе названия вещества и необходимого объема вы получите требуюмую массу', font='Helvetica 20')],
                # затем делаем текст
                [sg.Text('Введите название химическиго соединения', font='Helvetica 20')],
                [sg.Input(key='-ChemIN-')],
                [sg.Text('Введите концентрацию в молях', font='Helvetica 20')],
                [sg.Input(key='-ConcIN-')],
                [sg.Text('Введите объем в литрах', font='Helvetica 20')],
                [sg.Input(key='-SizeIN-')],
                [sg.Button('Посчитать', enable_events=True, key='-FUNCTION2-', font='Helvetica 16', visible='Жмякни меня и случится чудо')],
                [sg.Text('Здесь появится результат', key='-text2-', font='Helvetica 20')]
                 ]
        # что будет внутри окна следующего окна
        next_layout = []
        # Разметка вкладок
        layout =[[sg.TabGroup([[  sg.Tab('Преобразователь размерностей', convert_layout),
                                  sg.Tab('Химический калькулятор', buffer_layout),
                                  sg.Tab('В разработке', next_layout)]], key='-TAB GROUP-', expand_x=True, expand_y=True),
               ]]

        # рисуем окно, название и вкладки
        window = sg.Window('Ageldinov', layout)
        # запускаем основной бесконечный цикл
        while True:
                # получаем события, произошедшие в окне
                event, values = window.read()
                # если нажали на крестик
                if event in (sg.WIN_CLOSED, 'Exit'):
                        # выходим из цикла
                        break
                # если нажали на кнопку конвертации
                if event == '-FUNCTION-':
                      # запускаем связанную функцию
                     update()
                # если нажали на кнопку буферов
                elif event == '-FUNCTION2-':
                      # запускаем связанную функцию
                     buff()
        # закрываем окно и освобождаем используемые ресурсы

        window.close()

# На случай дополнений и запуск основной функции
if __name__ == '__main__':
        main()
