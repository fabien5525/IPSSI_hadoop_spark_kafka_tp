import sys
import json

# date,secousse,magnitude,tension entre plaque
json_file = json.load(sys.stdin)

json_clean = []

# Effectuez une analyse préliminaire pour détecter les événements sismiques en calculant l'amplitude des signaux.
# Identifiez les périodes d'activité sismique importante.

for item in json_file:
    # Supposon que l'amplitude = magnitude * tension entre plaque
    item['amplitude'] = float(item['magnitude']) * float(item['tension entre plaque']) 

    # Si l'amplitude est supérieure à 7, on ajoute la donnée à la liste
    if item['amplitude'] >= 7:
        json_clean.append(item)

print(json.dumps(json_clean))
