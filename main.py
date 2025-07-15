import sys
from stats import get_words, get_chars, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    final_list = sort_chars(get_chars(get_book_text(sys.argv[1])))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    print("----------- Word Count ----------")
    print(f"Found {get_words(get_book_text(sys.argv[1]))} total words")

    print("--------- Character Count -------")
    for item in final_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")


main()