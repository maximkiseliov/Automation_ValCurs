from filereader import get_dates
from getwebservice import get_data_from_webservice
from myxlswriterrr import xls_writer


datalist = get_dates('dates')
dictforxls = get_data_from_webservice(datalist)
xls_writer(dictforxls)
