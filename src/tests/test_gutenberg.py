import pytest
from bs4 import ResultSet

from gutenberg import group_by_lines, read_book_xml

@pytest.mark.parametrize("book_name", [
    ("iliad"),
    ("odyssey"),
])
def test_check_if_lines_are_parsed_correctly_for_all_books(book_name: str):
    for book_number in range(1,25):
        book = read_book_xml(book_name, book_number)
        assert book
        lines = group_by_lines(book)
        assert type(lines) is ResultSet
        for i, line in enumerate(lines):
            print(f"{book_name} {book_number}.{i+1} {line}")
            if ("n" in line.attrs):
                assert int(line.attrs["n"]) == i + 1
