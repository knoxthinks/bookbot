
def main():
    with open('books/frankenstein.txt') as f:

        file_contents = f.read()
        return(file_contents)

if __name__ == "__main__":
    main()

def count():
    words = len(main().split())
    print(words)

count()

# This was boot.dev solution

# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     print(text)


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()
# main()

# solution .9
# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     print(f"{num_words} words found in the document")


# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()


# main()


