import sys
import json

# date,secousse,magnitude,tension entre plaque
json_file = json.load(sys.stdin)

json_clean = []

# Utilisez des techniques de MapReduce pour trouver des corrélations entre différents événements sismiques. 
# Analysez si certains types d'événements sont précurseurs d'autres, plus importants.

for item in json_file:
    # magnitude moyenne
    item['magnitude moyenne'] = (float(item['magnitude']) + float(item['tension entre plaque'])) / 2
    # tension entre plaque moyenne
    item['tension entre plaque moyenne'] = (float(item['magnitude']) + float(item['tension entre plaque'])) / 2

    json_clean.append(item)

print(json.dumps(json_clean))
