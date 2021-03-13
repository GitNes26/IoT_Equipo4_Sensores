import json
from .. ..Classes.Sensor import Sensor
from .. ..Classes.Result import  Result

S = Sensor()
R = Result()
#ArrayList = []
listSensors = []
listResults = []
data = {}

def listsJSON(list):
    if list == 'sensors':
        data['sensorList'] = []
        dataJSON = 'dataSensors.json'
        nameList = 'sensorList'
    else:
        data['resultList'] = []
        dataJSON = 'dataResults.json'
        nameList = 'resultList'
    return (data, dataJSON, nameList)


def getId(list):
    data = listsJSON(list)
    with open('Scripts/DataJSON/'+data[1]) as f:
        listJSON = json.load(f)
        for i in listJSON[data[2]]:
            id = i['id']
        id += 1
    return id

def insert(list,  Object, id, sensor=None, sensor_id=None, data=None, create_at=None, update=None):
    data = listsJSON(list)
    getId(list)
    with open('Scripts/DataJSON/'+data[1]) as f:
        listJSON = json.load(f)
        for i in listJSON[data[2]]:
            id = i['id']