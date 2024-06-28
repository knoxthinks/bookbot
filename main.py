# my solution
book_path = 'books/frankenstein.txt'
def main():
    with open('books/frankenstein.txt') as f:

        file_contents = f.read()
        return(file_contents)

if __name__ == "__main__":
    main()

print(f"--- Being report of {book_path} ---")
def count():
    words = len(main().split())
    print(f"{words} words found in the document\n")

count()

def dicts():
    # book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lowercased = text.lower()
    answer = {}
    for char in lowercased:
        if char.isalpha(): 
            if char in answer:
                answer[char] += 1
            else:
                answer[char] = 1
    # print(answer)
    # Convert dictionary to a list of tuples and sort by the second item in each tuple (the count)
    sorted_counts = sorted(answer.items(), key=lambda item: item[1], reverse=True)
        # Print each character and its count on a new line
    for char, count in sorted_counts:
        print(f"The' {char}' character was found {count} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()

dicts()

print('--- End report ---')
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


