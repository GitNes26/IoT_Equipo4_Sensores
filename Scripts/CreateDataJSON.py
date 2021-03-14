import json
data = {}
'''
data['sensorList'] = []

data['sensorList'].append({
    'reg': 0
})

with open('DataJSON/dataSensors.json', 'w') as f:
    json.dump(data, f, indent=4)
'''
data['resultList'] = []

data['resultList'].append({
    'reg': 0
})

with open('DataJSON/dataResults.json', 'w') as f:
    json.dump(data, f, indent=4)