from gutenberg import group_by_lines, read_book_txt, read_book_xml


def print_poem_to_stdout(poem_name: str):
    line_sum = 0
    for book_number in range(1,25):
        xml = read_book_xml(poem_name, book_number)
        lines = group_by_lines(xml)
        text = [line.text for line in lines]
        for t in text:
            print(t)
        line_sum += len(text)

def process_poem(poem_name: str):
    text = read_book_txt(poem_name)
    print(text)

def process_iliad():
    poem_name = "iliad"
    process_poem(poem_name)

def process_odyssey():
    poem_name = "odyssey"
    process_poem(poem_name)

def main():
    process_iliad()

if __name__ == "__main__":
    main()

