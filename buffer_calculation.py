from molmass import Formula

#Функция второй вкладки для расчета буферов
def buff(values, window):
    # Переменные
    Chem = Formula(values['-FORMULA IN-'])
    Vol = values['-VOLUME IN-']    
    Conc = values['-CONCENTRATION IN-']
    # Рассчет
    Conc2 = float(Chem.mass) * float(Vol) * float(Conc)
    # Находим текст вывода и выводим в него все данные и результат
    text_elem = window['-RESULTS 2-']
    text_elem.update("Для получения {} с концентрацией {} M. и в объеме {} л. необходимо взять {} г. данного вещества".format(Chem, Conc, Vol, round(Conc2, ndigits=3)))
