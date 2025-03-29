from stats import get_word_count, get_letters, sort_dictionary

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    words = get_word_count(text)
    letters = get_letters(text)
    sorted_letters = sort_dictionary(text)

    print(f"{words} words found in the document")
    print(letters)
    print(sorted_letters)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()