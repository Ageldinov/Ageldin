#Функция второй вкладки для расчета буферов
def buff(values, window):
    # Переменные
    Chem = Formula(values['-ChemIN-'])
    Vol = values['-SizeIN-']    
    Conc = values['-ConcIN-']
    # Рассчет
    Conc2 = float(Chem.mass) * float(Vol) * float(Conc)
    # Находим текст вывода и выводим в него все данные и результат
    text_elem = window['-text2-']
    text_elem.update("Для получения {} с концентрацией {} M. в объеме {} л. необходимо взять {} г.".format(Chem, Conc, Vol, round(Conc2, ndigits=3)))
