
import streamlit as st
from docx import Document
import requests
from bs4 import BeautifulSoup

# Function to scrape public data
def scrape_data(name):
    # Simulate scraping data
    data = {
        "Name": name,
        "Court Cases": "No active court cases found.",
        "Debts": "No outstanding debts found.",
        "Criminal Record": "No criminal records found."
    }
    return data

# Function to create Word document
def create_word_report(data):
    doc = Document()
    doc.add_heading(f'Report for {data["Name"]}', level=1)
    doc.add_paragraph(f'Court Cases: {data["Court Cases"]}')
    doc.add_paragraph(f'Debts: {data["Debts"]}')
    doc.add_paragraph(f'Criminal Record: {data["Criminal Record"]}')
    filename = f'{data["Name"]}_report.docx'
    doc.save(filename)
    return filename

# Streamlit app interface
st.title("Person Background Checker")
name = st.text_input("Enter the name of the person:")

if st.button("Generate Report"):
    if name:
        data = scrape_data(name)
        report_file = create_word_report(data)
        st.success(f"Report for {name} generated!")
        with open(report_file, "rb") as file:
            st.download_button("Download Report", file, file_name=report_file)
    else:
        st.error("Please enter a name.")
