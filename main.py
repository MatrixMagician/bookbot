# This is a function to read contents of a file and return it
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

from stats import count_words, count_characters

def main():
    book_content = get_book_text("./books/frankenstein.txt")
    num_words = count_words(book_content)
    char_counts = count_characters(book_content)

    print(f"{num_words} words found in the document")
    print(char_counts)

main()