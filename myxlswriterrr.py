import xlsxwriter

def xls_writer(data_as_dict):
    header = ["ID", "NumCode", "CharCode", "Nominal", "Name", "Value"]
    workbook = xlsxwriter.Workbook('cursvaliut.xlsx')
    bold = workbook.add_format({'bold': True})
    
    #Создаю страницы название которых даты курса валют
    for key in data_as_dict.keys():
        worksheet = workbook.add_worksheet(key)
        row = 0 #Ряд
        col = 0 #Колонка     
        #Записываю в первую строку заголовки колонок
        for i in range(len(header)):
            worksheet.write(row, col+i, header[i], bold)
        row = 1 #Приравниваю к 1 потомучто 0ая строка занята headerom
        #Получаю доступ ко всем спискам словаря(в которых содержится информация об отдельных валютах)
        for item in data_as_dict[key]:
            #Прохожу по элементам списка(элементы отдельной валюты (e.g "ID", "NumCode")
            for j in item:
                worksheet.write(row, col, j)
                col += 1 #Переход на следующую колонку
            col = 0 #Обход списка валюты окончен поэтому сбрасываем колонку на 0
            row += 1 #Переходим на новую строку
        row = 0 #Обход списка списков валют окончен, перейдём на новую страницу

    workbook.close()

