# Функция первой вкладки для конвертации величин
def update(values, window):        
    # Задаем дефолтные значения
    num = values['-AMOUNT-']
    r = 1
    # получаем доступ к текстовому элементу
    text_elem = window['-RESULTS 1-']
    # Считываем значения с вкладки
    s1 = values['-UNIT OPTION START-']
    s2 = values['-UNIT OPTION END-']
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
    # Расчеты и вывод результатов
    r2 = r * float(num)
    # выводим в текст с новым числом
    return(text_elem.update("Результат: {} {} это {} {}".format(num, s1, round(r2, ndigits=9), s2)))