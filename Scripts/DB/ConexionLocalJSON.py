import json
from P2_Sensores.Classes.Sensor import Sensor
from P2_Sensores.Classes.Result import Result

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


def getReg(list):
    data = listsJSON(list)
    with open('Scripts/DataJSON/'+data[1]) as f:
        listJSON = json.load(f)
        for i in listJSON[data[2]]:
            reg = i['reg']
        reg += 1
    return reg

def insert(list,  Object, id, sensor=None, sensor_id=None, data=None, create_at=None, update=None):
    data = listsJSON(list)
    getReg(list)

    with open('Scripts/DataJSON/'+data[1]) as f:
        listJSON = json.load(f)
        for i in listJSON[data[2]]:
            reg = i['reg']