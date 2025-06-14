# This is a function to read contents of a file and return it
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

import sys
from stats import count_words, count_characters, sort_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_content = get_book_text(book_path)

    # Count the words in the book
    num_words = count_words(book_content)

    # Count the characters
    char_counts = count_characters(book_content)

    # Sort characters by count
    sorted_chars = sort_characters(char_counts)
    
    # Print the report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Print only alphabetical characters, sorted by count
    for char_data in sorted_chars:
        char = char_data["char"]
        num = char_data["num"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {num}")
    
    print("============= END ===============")

main()