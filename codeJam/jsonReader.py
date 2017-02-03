import json
import os.path


def getLecture():
    with open(os.path.dirname(__file__) + '/../classes.json', encoding = 'utf-8') as data_file:
        data = json.loads(data_file.read())
    return data

def getName():
    with open(os.path.dirname(__file__) + '/../studentsByAvailability.json', encoding = 'utf-8') as data_file:
        data = json.loads(data_file.read())
    
    #id = str(a)
    #sth = data[id][0]
    return data
