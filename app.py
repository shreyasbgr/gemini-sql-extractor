from dotenv import load_dotenv
import os
import streamlit as st
import sqlite3
import google.generativeai as genai
import pandas as pd

# Load environment variables
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to retrieve SQL response from the gemini model
def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content([prompt + question])
        return response.text
    except Exception as e:
        print(f"Error generating response from Gemini model: {e}")
        return None

# Function to retrieve query from the SQL database
def get_sql_response(sql_query, db_name):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute(sql_query)
        records = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        connection.commit()
        connection.close()
        return records, columns
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return None, None

# Define the prompt
prompt = """
You are an expert in converting natural language questions into SQL queries. The SQL database you will interact with has the following structure:

CREATE TABLE Student(
    name VARCHAR(25),
    class VARCHAR(25),
    section VARCHAR(25),
    marks INT
);

Given a question in English, convert it into a SQL query that accurately retrieves the requested information. Ensure the SQL code is well-formatted and easy to read. Do not include '```' or the word 'sql' in the output.

Here are some examples to guide you:

1. Question: 'How many students are there?'
   SQL Query: 'SELECT COUNT(*) FROM Student;'

2. Question: 'What is the highest marks scored by any student?'
   SQL Query: 'SELECT MAX(marks) FROM Student;'

3. Question: 'Show me the names of students who got more than 80 marks'
   SQL Query: 'SELECT name FROM Student WHERE marks > 80;'

Please generate an appropriate SQL query based on the question provided.
"""

# Streamlit App
st.set_page_config(page_title="SQL Query Extractor", page_icon=":books:")
st.header("Gemini App to retrieve SQL Data")
question = st.text_input("Enter your question:")
submit = st.button("Submit")

# If submit button is clicked
if submit:
    if question:
        sql_query = get_gemini_response(question, prompt)
        if sql_query:
            st.write("Generated SQL Query:")
            st.code(sql_query, language="sql")
            db_name = "student.db"
            records, columns = get_sql_response(sql_query, db_name)
            if records and columns:
                # Create a DataFrame to display the records
                df = pd.DataFrame(records, columns=columns)
                st.dataframe(df)
            else:
                st.write("No records found or error executing SQL query.")
        else:
            st.write("Error generating SQL query from the Gemini model.")
    else:
        st.write("Please enter a question")
