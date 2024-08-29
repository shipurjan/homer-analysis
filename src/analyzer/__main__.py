from pprint import pprint

from src.gutenberg import group_by_lines, read_book_xml


def main():
    xml = read_book_xml("iliad", 1)
    lines = group_by_lines(xml)
    pprint(lines[469])

if __name__ == "__main__":
    main()

