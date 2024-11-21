import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from Credentials import (
    POSTGRESQL_HOST,
    POSTGRESQL_PORT,
    POSTGRESQL_USER,
    POSTGRESQL_PASSWORD,
    POSTGRESQL_DATABASE
)

# Database Connection
db_config = {
    "username": POSTGRESQL_USER,
    "password": POSTGRESQL_PASSWORD,
    "host": POSTGRESQL_HOST,
    "port": POSTGRESQL_PORT,
    "database": POSTGRESQL_DATABASE
}
# connection_string = "postgresql://DanFaRa@rekdatsentimenanalysis:Qwerty123@rekdatsentimenanalysis.postgres.database.azure.com:5432/sentiment_analysis_etl?sslmode=require"
# engine = create_engine(connection_string)

# Create the database URL
db_url = f"postgresql+psycopg2://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}?sslmode=require"

# Create the SQLAlchemy engine
engine = create_engine(db_url, pool_pre_ping = True)

# Streamlit App
st.title("Sentiment Analysis Data Viewer")

# Query the database
query = "SELECT * FROM data_etl"
try:
    with engine.connect() as connection:
        df = pd.read_sql(query, connection)
        st.write("### Sentiment Analysis Data")
        st.dataframe(df)
except Exception as e:
    st.error(f"Error loading data: {e}")