from mysql_helper import MySQLHelper
import streamlit as st
import gemini_helper
import re

# Initialize the database helper
db = MySQLHelper(host="YouNeedToFillThis", user="YouNeedToFillThis", password="YouNeedToFillThis", database="YouNeedToFillThis")

# Connect to the database
db.connect()

def clean_sql_query(text):
    return re.sub(r"^```sql\s+|\s+```$", "", text, flags=re.DOTALL).strip()

q = st.text_input("Enter your query here")

if q:
    sql_query = gemini_helper.send_query(q)
    print(sql_query)
    if "tblcandidate" not in sql_query:
        st.write(sql_query)
    else:
        cleaned_query = clean_sql_query(sql_query)
        st.table(db.fetch_results(cleaned_query))
        db.close_connection()

