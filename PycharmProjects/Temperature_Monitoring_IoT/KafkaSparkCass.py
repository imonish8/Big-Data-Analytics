from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler

spark = SparkSession.builder.appName("IoTData").config("spark.cassandra.connection.host", "localhost").getOrCreate()
df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "temperature_data").load()

# Data Transformation
# Apply some transformations for temperature trend analysis and health scoring using MLlib