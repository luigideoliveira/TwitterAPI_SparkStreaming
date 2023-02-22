from pyspark.sql import SparkSession
import shutil

for item in ['./csv', './check']:
    try:
        shutil.rmtree(item)
    except OSError as err:
        print(f'Aviso: {err.strerror}')

spark = SparkSession.builder.appName('SparkStreaming').getOrCreate()

tweets = spark.readStream\
    .format('socket')\
    .option('host', 'localhost')\
    .option('port', 9008)\
    .load()

query = tweets.writeStream\
    .option('encoding', 'utf-8')\
    .format('csv')\
    .trigger(processingTime="10 seconds")\
    .option("path", "./csv")\
    .option("checkpointLocation", "./check")\
    .start()

query.awaitTermination()
