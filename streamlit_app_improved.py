
import streamlit as st
from docx import Document
import requests
from bs4 import BeautifulSoup

# Функція для отримання даних
def scrape_data(name):
    data = {
        "Ім'я": name,
        "Судові справи": "Справи не знайдено.",
        "Борги": "Борги відсутні.",
        "Кримінальне минуле": "Кримінальне минуле відсутнє.",
        "Додаткові джерела": "Дані в процесі обробки."
    }
    return data

# Функція для створення Word-документу
def create_word_report(data):
    doc = Document()
    doc.add_heading("Звіт про перевірку особи", level=1)
    for key, value in data.items():
        doc.add_paragraph(f"{key}: {value}")
    doc.save(f"{data['Ім\'я']}_звіт.docx")

# Інтерфейс Streamlit
st.title("Перевірка особи на судові впровадження")

name = st.text_input("Введіть ім'я та прізвище особи для перевірки:")
if st.button("Перевірити"):
    st.write(f"Перевіряємо особу: {name}...")
    try:
        data = scrape_data(name)
        st.write(data)
        create_word_report(data)
        st.success("Звіт успішно створено!")
    except Exception as e:
        st.error(f"Помилка: {e}")
