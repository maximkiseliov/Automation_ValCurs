from filereader import get_dates
from urllib import request
import xml.etree.ElementTree as ET

def get_data_from_webservice(listofdates):
    """Получение данных с веб сервиса"""
    cursdates = []
    onevalute = []
    allvalutes = []
    debil = []
    
    for i in listofdates:
        myURL = "https://bnm.md/en/official_exchange_rates?get_xml=1&date="+i
        otvet = request.urlopen(myURL)
        informatzia = otvet.read().decode()
        
   
        valcurs = ET.fromstring(informatzia)
        curstdate = valcurs.get('Date')#Дата курса
        cursdates.append(curstdate)
        lst = valcurs.findall('Valute')#список тегов (валют)

        for valdata in lst:
            id_valut = valdata.get('ID')
            onevalute.append(id_valut)
            
            numcode = valdata.find('NumCode').text
            onevalute.append(numcode)
            
            charcode = valdata.find('CharCode').text
            onevalute.append(charcode)
            
            nominal = valdata.find('Nominal').text
            onevalute.append(nominal)
            
            name = valdata.find('Name').text
            onevalute.append(name)
            
            value_valut = valdata.find('Value').text
            onevalute.append(value_valut)

            allvalutes.append(onevalute)
            onevalute = []
        debil.append(allvalutes)
        allvalutes = []


        
    my_dict = dict(zip(cursdates, debil))
    return my_dict
