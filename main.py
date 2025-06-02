from stats import num_words
from stats import num_character
from stats import sorted_dict
from sys import argv
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        string = f.read()
    return string

def main(get_book_text):
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = argv[1]
             
    total_words = get_book_text(file_path)
    total = num_words(total_words)
    total_dict = num_character(total_words)
    sorted_dictionary = sorted_dict(total_dict)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {total} total words")
    print("--------- Character Count -------")
    for char in sorted_dictionary:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
    return total_words


main(get_book_text)


