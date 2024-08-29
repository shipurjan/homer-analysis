import os
import re

from bs4 import BeautifulSoup

abspath = os.path.abspath(os.path.dirname(__file__))

def read_book_txt(poem_name: str):
    with open(os.path.join(abspath, "..", "..", "data", f"{poem_name}.txt")) as f:
        return f.read()

def read_book_xml(poem_name: str, book_number: int = 1):
    with open(os.path.join(abspath, "..", "..", "data", poem_name, f"book_{book_number}.xml")) as f:
        return f.read()

def group_by_lines(xml: str):
    soup = BeautifulSoup(xml, "xml")
    return soup.find_all("l")

