from pyspark.sql import SparkSession, functions as f
import shutil

spark = SparkSession.builder.appName('SparkStreaming').getOrCreate()

lines = spark.readStream\
    .format('socket')\
    .option('host', 'localhost')\
    .option('port', 9008)\
    .load()

words = lines.select(f.explode(f.split(lines.value, ' ')).alias('word'))

wordCounts = words.groupBy('word').count().orderBy('count', ascending=False)

query = wordCounts.writeStream\
    .option('encoding', 'utf-8')\
    .outputMode('complete')\
    .format('console')\
    .start()

query.awaitTermination()
