import os
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from dotenv import load_dotenv

def connectToSnowflake(df):
    # Enable debug logging
    snowflake.connector.paramstyle = 'qmark'
    snowflake.connector.connection.logger.setLevel('DEBUG')

    # Create a connection object
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),           
        password=os.getenv('SNOWFLAKE_PASSWORD'),    
        account=os.getenv('SNOWFLAKE_ACCOUNT'),       
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA')
    )

    # LOAD DATA INTO SNOWFLAKE
    success, nchunks, nrows, _ = write_pandas(conn, df, 'ALCOHOL_CONSUMPTION', auto_create_table=True)

    if success:
        print(f'Loaded {nrows} rows into table ALCOHOL_CONSUMPTION')
    else:
        print('Error loading data into Snowflake')

    # Close the connection
    conn.close()