import sys
import json

list = []
columns = []

for index, csv_line in enumerate(sys.stdin):
    sep = ','
    csv_line = csv_line.strip()
    csv = csv_line.split(sep)
    
    # Si c'est la première ligne, on récupère les colonnes
    if index == 0:
        columns = csv
        continue

    # On crée un dictionnaire avec les colonnes en clé
    # list = [{ 'date': '2018-01-01', 'secousse': 'True', 'magnitude': '7.0', 'tension entre plaque': '0.0' }]
    item = {}
    for i, column in enumerate(columns):
        item[column] = csv[i]

    # On ajoute l'item à la liste
    list.append(item)

print(json.dumps(list))