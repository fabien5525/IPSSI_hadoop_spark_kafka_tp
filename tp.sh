# Partie 1 : Exploration et Traitement des Données Sismiques avec Hadoop

# Exercice 1 : Configuration de l'Environnement Docker
echo -e "\n\n Lancement des containers"

docker compose down -v
docker compose up -d

# sleep 5s to wait containers to start
sleep 5s

# Exercice 2 : Importation et Exploration des Données Sismiques
# * Création d'un dossier avec hadoop / hdfs
docker compose exec hadoop-namenode bash -c 'cd /app
echo -e "\n\n Contenu du dossier /app"
ls -l

echo -e "\n\n Import de /app/dataset_sismique.csv dans HDFS"
hadoop fs -mkdir /data
hadoop fs -put /app/dataset_sismique.csv /data
hadoop fs -ls /data

echo -e "\n\n Lecture fichier dataset_sismique.csv"
hadoop fs -cat /data/dataset_sismique.csv | head -n 10
'

# Exercice 3 : Nettoyage des Données avec Hadoop
# * Exécution du script de nettoyage des données (map & reduce)
echo -e "\n\n Nettoyage des données avec Hadoop"
## Avec docker
# docker compose exec hadoop-namenode bash -c 'cd /app
# pip install -r requirements.txt
# hadoop fs -cat /data/dataset_sismique.csv | ./mapred_ex3/map.py | ./mapred_ex3/reduce.py > /app/dataset_sismique_cleaned_ex3.csv
# '
## En local
python -m venv .venv # ça peu échoué avec des problèmes de droits
PYTHON_PATH='.venv/Scripts/python'
cat ./app_hadoop/dataset_sismique.csv | $PYTHON_PATH ./app_hadoop/mapred_ex3/map.py | $PYTHON_PATH ./app_hadoop/mapred_ex3/reduce.py > ./app_hadoop/dataset_sismique_cleaned_ex3.json

# Mise du fichier nettoyé dans HDFS
echo -e "\n\n Import de /app/dataset_sismique_cleaned_ex3.json dans HDFS"
docker compose exec hadoop-namenode bash -c 'cd /app
hadoop fs -put /app/dataset_sismique_cleaned_ex3.json /data
hadoop fs -ls /data
hadoop fs -cat /data/dataset_sismique_cleaned_ex3.json | head -c 100
'

# Exercice 4 : Analyse Préliminaire des Événements Sismiques
## En local
echo -e "\n\n Analyse préliminaire des événements sismiques"
cat ./app_hadoop/dataset_sismique_cleaned_ex3.json | $PYTHON_PATH ./app_hadoop/mapred_ex4/map.py | $PYTHON_PATH ./app_hadoop/mapred_ex4/reduce.py > ./app_hadoop/dataset_sismique_analysis_ex4.json
docker compose exec hadoop-namenode bash -c 'cd /app && cat /app/dataset_sismique_analysis_ex4.json | head -c 100'

# Exercice 5 : Corrélation des Événements Sismiques
## En local
echo -e "\n\n Corrélation des événements sismiques"
cat ./app_hadoop/dataset_sismique_cleaned_ex3.json | $PYTHON_PATH ./app_hadoop/mapred_ex5/map.py | $PYTHON_PATH ./app_hadoop/mapred_ex5/reduce.py > ./app_hadoop/dataset_sismique_correlation_ex5.json
docker compose exec hadoop-namenode bash -c 'cd /app && cat /app/dataset_sismique_correlation_ex5.json | head -c 100'

# Exercice 6 : Agrégation des Données Sismiques
## En local
echo -e "\n\n Agrégation des données sismiques"
cat ./app_hadoop/dataset_sismique_cleaned_ex3.json | $PYTHON_PATH ./app_hadoop/mapred_ex6/map.py | $PYTHON_PATH ./app_hadoop/mapred_ex6/reduce.py > ./app_hadoop/dataset_sismique_aggregation_ex6.json
docker compose exec hadoop-namenode bash -c 'cd /app && cat /app/dataset_sismique_aggregation_ex6.json | head -c 100'

# Partie 2 : Analyses Temporelles Avancées avec Spark

# Exercice 7 : Intégration de Spark & Exercice 8 : Analyse Temporelle Approfondie
echo -e "\n\n Analyse avec Spark"
docker compose exec spark-master bash -c 'cd /app
apk add py3-numpy
pip install -r requirements.txt
/spark/bin/spark-submit ./ex8.py
'

# Partie 3 : Surveillance en Temps Réel avec Kafka

# Exercice 9 : Configuration de Kafka pour le Streaming de Données & Exercice 10 : Streaming Analytics avec Spark Streaming
echo -e "\n\n Streaming avec Kafka"

# Lancer le producer (kafka), émettre des strings (de json) dans le flux de kafka (topic: topic1)
# docker compose exec kafka bash -c 'cd /app && ./start.sh'

# Lancer le consumer (spark-master) pour lire les messages du topic topic1
# docker compose exec spark-master bash -c 'cd /app
# /spark/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 ./ex10.py
# '