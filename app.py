import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Database Connection
connection_string = "postgresql://DanFaRa@rekdatsentimenanalysis:Qwerty123@rekdatsentimenanalysis.postgres.database.azure.com:5432/sentiment_analysis_etl?sslmode=require"
engine = create_engine(connection_string)

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