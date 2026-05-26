import os
from pyspark.sql import SparkSession

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("SimplePySpark") \
    .getOrCreate()

data = [
    ("Abhishek", 24),
    ("Rahul", 25)
]

df = spark.createDataFrame(data, ["Name", "Age"])

df.show()

spark.stop()