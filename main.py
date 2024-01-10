import os
import openai
from llama_index import SQLDatabase
from llama_index.indices.struct_store import (
    NLSQLTableQueryEngine,
    SQLTableRetrieverQueryEngine,
)
from sqlalchemy import create_engine

os.environ['OPENAI_API_KEY'] = '<your_openai_api_key_here>'
openai.api_key="<your_openai_api_key_here>"

engine = create_engine("mssql+pyodbc://user:password@server/database")

# Connect llamindex to the SQL engine, naming the table we will use
sql_database = SQLDatabase(engine, include_tables=["Table1"])

# Create a structured store to offer a context to GPT
query_engine = NLSQLTableQueryEngine(sql_database)

# Invoke query_engine to ask a question and get answer
response = query_engine.query("User Question")
str(response)
