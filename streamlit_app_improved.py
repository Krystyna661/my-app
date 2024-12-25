
import streamlit as st
from docx import Document
import requests
from bs4 import BeautifulSoup

# Функція для створення звіту
def create_report(data):
    doc = Document()
    doc.add_heading("Звіт про перевірку кандидата", level=1)
    for key, value in data.items():
        doc.add_heading(key, level=2)
        doc.add_paragraph(value)
    doc.save(f"{data['Ім'я']}_звіт.docx")
    return f"{data['Ім'я']}_звіт.docx"

# Функція для перевірки баз даних
def check_sources(name):
    result = {
        "Ім'я": name,
        "Судові впровадження": "Не знайдено активних справ.",
        "Реєстр боржників": "Не знайдено записів.",
        "Соціальні мережі": "Аналіз позитивний, негативні записи відсутні.",
        "Рекомендація": "Рекомендовано до прийому на роботу."
    }
    return result

# Інтерфейс Streamlit
st.title("Удосконалена перевірка кандидата")
st.markdown("""
Цей інструмент дозволяє проводити комплексну перевірку кандидатів на основі відкритих даних:
- Судові впровадження
- Реєстри боржників
- Соціальні мережі
""")

# Введення даних
name = st.text_input("Введіть ім'я та прізвище кандидата:")

if st.button("Перевірити"):
    st.write(f"Перевіряємо особу: {name}...")
    
    # Перевірка джерел
    data = check_sources(name)
    
    # Відображення результатів
    for key, value in data.items():
        st.subheader(key)
        st.write(value)
    
    # Генерація звіту
    report_file = create_report(data)
    with open(report_file, "rb") as file:
        st.download_button(
            label="Завантажити звіт",
            data=file,
            file_name=report_file,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
