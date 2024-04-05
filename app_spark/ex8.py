# coding: utf-8

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

# Initialisation de SparkSession
spark = SparkSession.builder.appName("writeHDFS").getOrCreate()
sc = spark.sparkContext
sc.setLogLevel("WARN")

# Lecture des données depuis HDFS
df = spark.read.json("hdfs://namenode:9000/data/dataset_sismique_cleaned_ex3.json")

# Convertir les colonnes en types numériques
df = df.withColumn("magnitude", col("magnitude").cast("double"))
df = df.withColumn("tension entre plaque", col("tension entre plaque").cast("double"))

# Supprimer les lignes contenant des valeurs nulles (si nécessaire)
df = df.na.drop()

# Convertir les colonnes en vecteur
assembler = VectorAssembler(
    inputCols=["magnitude", "secousse", "tension entre plaque"],
    outputCol="features")

df_assembled = assembler.transform(df)

# Entraîner le modèle K-Means
kmeans = KMeans().setK(2).setSeed(1)
model = kmeans.fit(df_assembled)

# Faire des prédictions
predictions = model.transform(df_assembled)

# Évaluer la performance en utilisant l'evaluateur de clustering
evaluator = ClusteringEvaluator()
silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))

# Afficher les centres des clusters
centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)

# Arrêt de la session Spark
spark.stop()
