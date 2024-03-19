def main():
    book_path = "/home/vincent/workspace/github.com/Bravoeen/bookbot/.gitignore/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = count_letters(text)
    print(f"{num_words} words found in the document")
    print(char_dict)

#splits words counts them
def get_num_words(text):
    words = text.split()
    return len(words)

#reads the book returns a string
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def count_letters(text):
    lowered_words = text.lower()
    num_chars = {}

    for char in lowered_words:
        if char.isalpha():
            if char in num_chars:
                num_chars[char] += 1
            else:
                num_chars[char] = 1

    return num_chars
    
    
main()