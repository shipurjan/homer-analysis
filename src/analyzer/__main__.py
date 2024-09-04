
from cltk import NLP

from gutenberg import group_by_lines, read_book_txt, read_book_xml

cltk_nlp = NLP(language="grc", suppress_banner=True)
cltk_nlp.pipeline.processes.pop(-1)

def print_poem_to_stdout(poem_name: str):
    for book_number in range(1,25):
        xml = read_book_xml(poem_name, book_number)
        lines = group_by_lines(xml)
        text = [line.text for line in lines]
        for t in text:
            print(t)

def rm_char(original_str: str, need2rm: str):
    ''' Remove characters in "need2rm" from "original_str" '''
    return original_str.translate(str.maketrans('','',need2rm))

def remove_greek_punctuation(greek_text: str):
    return rm_char(greek_text, ".,:;'")

def cltk(long_text: str):
    print("Analyzing...")
    text = long_text[:len(long_text) // 60]
    cltk_doc = cltk_nlp.analyze(text=text)
    return cltk_doc


def get_frequency_list(poem_name: str):
    text = read_book_txt(poem_name)
    text = remove_greek_punctuation(text)
    text = cltk(text)
    return text
    # wordlist = text.split()
    # return Counter(wordlist)

def process_poem(poem_name: str):
    freq = get_frequency_list(poem_name)
    print(freq)

def main():
    process_poem("iliad")

if __name__ == "__main__":
    main()

