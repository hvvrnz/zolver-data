from src.sources.pdf_reader import pdf_to_text
from src.parsing.newline_normalizer import newline_normalize
from src.preprocessing.required_credits import extract_table_text, result_rows


def main(year: int, page_num: int):
    raw_text = pdf_to_text(year, page_num)
    normalized_text = newline_normalize(raw_text)
    table_text = extract_table_text(normalized_text)
    rows = result_rows(table_text)

    return rows


if __name__ == "__main__":
    rows = main(2021, 5)

    for r in rows:
        print(r)