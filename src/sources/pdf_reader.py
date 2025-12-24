import pandas as pd 
import requests
import fitz  # PyMuPDF 라이브러리 / pdf 열기/읽기
from PIL import Image
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2] #project root

def pdf_to_text(year,page_num):
    pdf_path = BASE_DIR / "data" / "pdfs" / "final" / f"{year}.pdf"
    pdf = fitz.open(pdf_path)
    page = pdf.load_page(page_num)
    text = page.get_text()
    pdf.close()
    return text
