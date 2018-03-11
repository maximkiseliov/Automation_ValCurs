def get_dates(filename):
    '''Считывает данные из файла и возвращает даты в виде списка'''
    file = open(filename+'.txt', 'r')
    datastring = file.read().strip()
    file.close()
    datalist = datastring.split('\n')
    return datalist

