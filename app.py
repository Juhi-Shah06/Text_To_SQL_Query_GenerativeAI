from dotenv import load_dotenv
load_dotenv()  # load all the environment variables

import streamlit as st
import os
import sqlite3

import logging 
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

import google.generativeai as genai

## Configure Genai key

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and provide query as response

def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content([prompt[0], question])
        return response.text
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        return None

# Function to retrieve query from the database

def read_sql_query(sql, db):
    try:
        sql_connect = sqlite3.connect(db)
        sql_cursor = sql_connect.cursor()
        sql_cursor.execute(sql)
        rows = sql_cursor.fetchall()
        sql_connect.commit()
        sql_connect.close()
        for row in rows:
            print(row)
        return rows
    except Exception as e:
        logger.error(f"Error executing SQL query: {e}")
        return None

# Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query. 
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION 
    \n\n For example: \n Example1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    Example2 - Tell me the students who have got more than 95 marks., 
    the SQL command will be something like this 
    SELECT * FROM STUDENT WHERE MARKS > 90;
    Example3 - How many students have opted for AI/ML class?
    the sql command will be something like this
    SELECT NAME FROM STUDENT WHERE CLASS = "AI/ML";
    also the SQL code should not have ''' in the beginning or end and sql word in the output.
    """
]

# Streamlit App

st.set_page_config(page_title= "SQL Query")
st.header("Gemini App to retrieve SQL data")

question = st.text_input("Input: ",key = "Input")

submit = st.button("Ask the question")

# if submit is clicked

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, "student.db")
    st.subheader("The response is")
    for row in response:
        print(row)
        st.header(row)