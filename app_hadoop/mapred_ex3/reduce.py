import sys
import json

# date,secousse,magnitude,tension entre plaque
json_file = json.load(sys.stdin)

json_clean = []

for item in json_file:
    # Ne pas prendre si la tension entre plaque est de 0.0
    if item['tension entre plaque'] == 0.0:
        continue

    # transformer la secousse en 0 ou 1
    if item['secousse'] == 'True':
        item['secousse'] = 1
    else:
        item['secousse'] = 0

    # Ajouter a la liste
    json_clean.append(item)

print(json.dumps(json_clean))
