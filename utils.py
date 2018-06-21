from datetime import datetime

def str_to_datetime(date):
    if type(date) != str:
        return date
    
    return datetime.strptime(date, '%d/%m/%Y %H:%M')
    