import json

#ArrayList = []
data = {}

def listsJSON(table):
    if table == 'sensors':
        data['sensorList'] = []
        dataJSON = 'dataSensors.json'
    else:
        data['resultList'] = []
        dataJSON = 'dataResults.json'
    return (data, dataJSON)


def getId(table, dataJSON):
    data = listsJSON(table)
    with open('Scripts/DataJSON/'+data[1]) as f:
        listJSON = json.load(f)
        for i in listJSON['sensorList']:
            id = i['id']
        id += 1
    return id

def insert(list, dataJSON,  Object, id, sensor=None, sensor_id=None, data=None, create_at=None, update=None):
    with open('Scripts/DataJSON/'+dataJSON) as f:
        listJSON = json.load(f)
        for i in listJSON['sensorList']:
            id = i['id']