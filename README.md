# Automation_ValCurs
Чтение дат с файла. Запрос по датам. Парсинг XML. Запись данных в xls.

Задание:
1. Read a set of dates from file (txt/csv)
2. Use these dates as parameters to request currency rates from BNM site (https://bnm.md/en/official_exchange_rates?get_xml=1&date=13.02.2018)
3. Create a list of objects based on received values
4. Save these values on separate page for each date in xls/xlsx file

Реализация:
1. Чтения дат из файла реализуется в "filereader.py". Чтение производится из файла "dates.txt". Каждая новая дата должна быть прописана с новой строки.
2. Запрос и парсинг полученных данных реализован в "getwebservice.py" . 
3. Передача распарсенных данных и запись в xls реализованы в "myxlswriterrr.py". Создаётся новый файл "cursvaliut.xlsx" с полученными данными.
4. Все вышеперечисленное собрано и может быть запущенно из файла "main.py".

NOTE:
Для запуска могут понадобится сторонние библиотеки, которые необходимо скачать отдельно при помощи консольной команды pip install library_name .
Библиотеки:
xlsxwriter -> pip install XlsxWriter
