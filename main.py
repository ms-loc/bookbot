from stats import count_words, sort_letters
from stats import count_letters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
            
    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)
    
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    
    print("--------- Character Count -------")
    l_array = sort_letters(count_letters(text))
    for l in l_array:
        print(f"{l["letter"]}: {l["num"]}")
    
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()