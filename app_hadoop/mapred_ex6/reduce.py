import sys
import json

# date,secousse,magnitude,tension entre plaque
json_file = json.load(sys.stdin)

json_clean = []

# Agrégé les données sur différents intervalles de temps pour observer les tendances de l'activité sismique.
# Cela peut aider à identifier des modèles ou des anomalies saisonnières ou périodiques dans les données.

for item in json_file:
    # somme magnitude
    item['somme magnitude'] = float(item['magnitude']) + float(item['tension entre plaque'])
    # somme tension entre plaque
    item['somme tension entre plaque'] = float(item['magnitude']) + float(item['tension entre plaque'])
    # moyenne magnitude
    item['moyenne magnitude'] = (float(item['magnitude']) + float(item['tension entre plaque'])) / 2
    # moyenne tension entre plaque
    item['moyenne tension entre plaque'] = (float(item['magnitude']) + float(item['tension entre plaque'])) / 2

    json_clean.append(item)

# ordronner les données par date
json_clean = sorted(json_clean, key=lambda x: x['date'])

# les regrouper par tranche de 15 minutes
# {'00:00' : {}, '00:15', ...} 
json_grouped = {}
for item in json_file:
    date = item['date']
    time = date.split(' ')[1]
    time = time.split(':')
    hour = time[0]
    minute = time[1]
    minute = int(minute) - (int(minute) % 15)
    minute = str(minute)
    if len(minute) == 1:
        minute = '0' + minute
    time = hour + ':' + minute
    if time not in json_grouped:
        json_grouped[time] = []
    json_grouped[time].append(item)

print(json.dumps(json_grouped))
