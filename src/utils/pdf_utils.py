import pandas as pd 
import requests
import fitz  # PyMuPDF 라이브러리 / pdf 열기/읽기
from PIL import Image

# 추후 전 년도 적용 가능하도록 자동화 예정 일단 2021만
def pdf_to_text(year,page_num):
    pdf = fitz.open(f"../data/pdfs/final/{year}.pdf")
    page = pdf.load_page(page_num)
    text = page.get_text()
    pdf.close()
    return text
