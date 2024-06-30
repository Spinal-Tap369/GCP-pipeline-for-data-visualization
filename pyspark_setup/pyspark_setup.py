from pyspark.sql.types import *
from pyspark.sql.functions import col, to_timestamp

schema = StructType([
    StructField("Id", IntegerType(), True),
    StructField("order_status", StringType(), True),
    StructField("order_products_value", DoubleType(), True),
    StructField("order_freight_value", DoubleType(), True),
    StructField("order_items_qty", IntegerType(), True),
    StructField("customer_city", StringType(), True),
    StructField("customer_state", StringType(), True),
    StructField("customer_zip_code_prefix", IntegerType(), True),
    StructField("product_name_length", IntegerType(), True),
    StructField("product_description_length", IntegerType(), True),
    StructField("product_photos_qty", IntegerType(), True),
    StructField("review_score", IntegerType(), True),
    StructField("order_purchase_timestamp", StringType(), True),
    StructField("order_approved_at", StringType(), True),
    StructField("order_delivered_customer_date", StringType(), True)
])

df = spark.read.format("csv").option("sep", ",").option("header", "true").schema(schema).load("hdfs:///user/ecom-project/ecom-dataset.csv")

# Transform data (timestamps, day, week)
df = df.withColumn("order_purchase_timestamp", to_timestamp(col("order_purchase_timestamp"), "dd-MM-yy HH:mm")) \
       .withColumn("order_approved_at", to_timestamp(col("order_approved_at"), "dd-MM-yy HH:mm")) \
       .withColumn("order_delivered_customer_date", to_timestamp(col("order_delivered_customer_date"), "dd-MM-yy HH:mm"))
from pyspark.sql import functions as F

df = df.withColumn("day", F.dayofmonth("order_purchase_timestamp"))
df = df.withColumn("week", F.weekofyear("order_purchase_timestamp"))
