
import streamlit as st
from docx import Document
import requests

def scrape_data(name):
    # Емуляція збору даних
    return {
        "Ім'я": name,
        "Судові справи": "Не знайдено активних судових справ.",
        "Борги": "Боргів не виявлено.",
        "Кримінальна історія": "Кримінальних записів не знайдено."
    }

def create_word_report(data):
    doc = Document()
    doc.add_heading('Звіт про перевірку особи', level=1)
    doc.add_paragraph(f"Ім'я: {data['Ім\'я']}")
    doc.add_paragraph(f"Судові справи: {data['Судові справи']}")
    doc.add_paragraph(f"Борги: {data['Борги']}")
    doc.add_paragraph(f"Кримінальна історія: {data['Кримінальна історія']}")
    filename = f"{data['Ім\'я']}_звіт.docx"
    doc.save(filename)
    return filename

st.title("Перевірка особи на судові впровадження")
st.write("Цей застосунок допомагає перевірити особу на наявність судових впроваджень та інших важливих даних.")

name = st.text_input("Введіть ім'я та прізвище особи для перевірки:")
if st.button("Перевірити"):
    if name:
        st.write(f"Перевіряємо особу: {name}...")
        data = scrape_data(name)
        st.write("Результати перевірки:")
        st.write(f"Ім'я: {data['Ім\'я']}")
        st.write(f"Судові справи: {data['Судові справи']}")
        st.write(f"Борги: {data['Борги']}")
        st.write(f"Кримінальна історія: {data['Кримінальна історія']}")
        
        report_filename = create_word_report(data)
        with open(report_filename, "rb") as file:
            btn = st.download_button(
                label="Завантажити звіт",
                data=file,
                file_name=report_filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    else:
        st.error("Будь ласка, введіть ім'я та прізвище.")
