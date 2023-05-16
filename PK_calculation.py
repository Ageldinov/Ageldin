#Функция третьей вкладки для расчета буферов
def PK_cal():
    df = pd.read_excel(str(folder_or_file))
    '''
    # Находим текст вывода и выводим в него все данные и результат
    text_elem = window['-text2-']
    text_elem.update("Для получения {} с концентрацией {} M. в объеме {} л. необходимо взять {} г.".format(Chem, Conc, Vol, round(Conc2, ndigits=3)))
    df.plot(x ='year', y='unemployment_rate', kind='line')
    df.plot.pie(y='tasks', figsize=(5, 5), autopct='%1.1f%%', startangle=90)
    plt.show()
    '''
    sg.popup(df)
    text_elem = window['-text20-']
    text_elem.update("Для получения {} с концентрацией {} M. в объеме {} л. необходимо взять {} г.".format(Chem, Conc, Vol, round(Conc2, ndigits=3)))
