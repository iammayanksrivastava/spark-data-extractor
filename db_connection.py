from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils

def get_dbutils(spark: SparkSession):
    try:
        from pyspark.dbutils import DBUtils  # type: ignore

        dbutils = DBUtils(spark)
    except ImportError:
        import IPython  # type: ignore

        dbutils = IPython.get_ipython().user_ns["dbutils"]
    return dbutils


secret_scope        = "cy05jv"
server_name_secret  = "jdbchostname"
username_secret     = "jdbcusername"
password_secret     = "jdbcpassword"

def fetch_db_config():
    dbutils = get_dbutils(None)

    jdbchostname = dbutils.secrets.get(scope=secret_scope, key=server_name_secret)
    jdbcusername = dbutils.secrets.get(scope=secret_scope, key=username_secret)
    jdbcpassword = dbutils.secrets.get(scope=secret_scope, key=password_secret)
    server_name = "jdbc:sqlserver://"+ jdbchostname
    database_name = "AdventureWorksDW"
    jdbcurl = server_name + ";" + "databaseName=" + database_name

    return jdbcurl, jdbchostname, jdbcusername, jdbcpassword
