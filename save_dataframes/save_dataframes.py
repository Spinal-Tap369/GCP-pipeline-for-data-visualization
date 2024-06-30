# Save DataFrames to GCS as CSV
df1.coalesce(1).write.mode("overwrite").option("header", "true").csv("gs://ecom-buck2806/processed_data1")
df2.coalesce(1).write.mode("overwrite").option("header", "true").csv("gs://ecom-buck2806/processed_data2")
df3.coalesce(1).write.mode("overwrite").option("header", "true").csv("gs://ecom-buck2806/processed_data3")
df4.coalesce(1).write.mode("overwrite").option("header", "true").csv("gs://ecom-buck2806/processed_data4")
df5.coalesce(1).write.mode("overwrite").option("header", "true").csv("gs://ecom-buck2806/processed_data5")

# Save DataFrames to Hive Tables
spark.sql("USE ecom_project")
df1.write.mode("overwrite").saveAsTable("ecom_project.df1")
df2.write.mode("overwrite").saveAsTable("ecom_project.df2")
df3.write.mode("overwrite").saveAsTable("ecom_project.df3")
df4.write.mode("overwrite").saveAsTable("ecom_project.df4")
df5.write.mode("overwrite").saveAsTable("ecom_project.df5")

# Save DataFrames to HDFS as CSV
df1.write.mode("overwrite").option("header", "true").csv("hdfs:///user/ecom-project/df1")
df2.write.mode("overwrite").option("header", "true").csv("hdfs:///user/ecom-project/df2")
df3.write.mode("overwrite").option("header", "true").csv("hdfs:///user/ecom-project/df3")
df4.write.mode("overwrite").option("header", "true").csv("hdfs:///user/ecom-project/df4")
df5.write.mode("overwrite").option("header", "true").csv("hdfs:///user/ecom-project/df5")
