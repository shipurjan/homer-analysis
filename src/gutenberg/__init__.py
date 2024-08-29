import os
import re

from bs4 import BeautifulSoup

abspath = os.path.abspath(os.path.dirname(__file__))

def read_book_xml(poem_name: str, book_number: int = 1):
    with open(os.path.join(abspath, "..", "..", "data", poem_name, f"book_{book_number}.xml")) as f:
        return f.read()

def read_poem_xml(poem_name: str, book_count: int = 24):
    return [read_book_xml(poem_name, i) for i in range(1,book_count+1)]

def group_by_lines(xml: str):
    soup = BeautifulSoup(xml, "xml")
    return soup.find_all("l")

def split_text_by_cards(xml: str):
    return re.split(r'<milestone.*unit="card".*/>', xml, flags=re.IGNORECASE)

def split_card_by_paragraphs(card_xml: str):
    result = re.split(r'(.*)<milestone.*unit="para".*/>', card_xml, flags=re.IGNORECASE)

    def concat_with_first_element(list: list, s: str):
        return [list[0] + s if len(list) != 0 else s] + list[1:]

    first = result[0]
    paragraphs = result[1:]

    if (len(paragraphs) == 1):
        return concat_with_first_element(paragraphs, first)

    if (len(paragraphs) % 2 == 1):
        raise Exception("Unexpected paragraphs length. Expected even number of elements.")

    joined = [a + b for a,b in zip(paragraphs[0::2], paragraphs[1::2])]
    return concat_with_first_element(joined, first)



def get_parsed_book(poem_name: str, book_number: int =1):
    xml = read_book_xml(poem_name, book_number)
