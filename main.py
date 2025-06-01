# This is a function to read contents of a file and return it
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_content = get_book_text("./books/frankenstein.txt")
    print(book_content)

main()