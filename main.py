from pyspark.sql import SparkSession, DataFrame
from db_connection import fetch_db_config
from pyspark.context import SparkContext
from pyspark import sql
from IPython.display import display



##Fetch Data from delta table into Data frame
def fetch_data_from_delta(
  spark: SparkSession, 
  sql: sql
  ): 
  global dfRep
  df = spark.sql("select * from lending_club_acc_loans limit 100000")
  dfRep = df.repartition(8)
  return dfRep

def load_df_to_db():
  
  jdbchostname, jdbcurl, jdbcusername, jdbcpassword = fetch_db_config()

  try:
    dfRep.write \
      .format("com.microsoft.sqlserver.jdbc.spark") \
      .mode("overwrite") \
      .option("url", jdbchostname) \
      .option("dbtable", "lending_club_acc_loans") \
      .option("user", jdbcusername) \
      .option("password", jdbcpassword) \
      .option("tableLock", "true") \
      .option("batchsize", "50000") \
      .option("reliabilityLevel", "BEST_EFFORT") \
      .save()

  except ValueError as error :
      print("Connector write failed", error)


def run():
  spark = SparkSession.builder.getOrCreate()

  fetch_data_from_delta(spark, sql)

  load_df_to_db()


if __name__ == "__main__":
    run()