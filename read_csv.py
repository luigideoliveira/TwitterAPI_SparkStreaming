from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('ReadCSV').getOrCreate()

df = spark.read.csv('./csv')

df.show()