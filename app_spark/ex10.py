from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkApp").getOrCreate()
sc = spark.sparkContext.setLogLevel("WARN")


# Consumer code
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "topic1") \
    .option("maxRequestSize", "1073741824") \
    .load()

df = df.selectExpr("CAST(value AS STRING)")

query = df.writeStream.outputMode("append").format("console").start()
query.awaitTermination()