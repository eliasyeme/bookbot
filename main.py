def count_words(text):
    return len(text.split())


def count_letters(text):
    counted = {}
    for letter in text:
        key = letter.lower()
        val = counted.get(key, 0) + 1
        counted[key] = val
    return counted


def main():
    with open("books/frankenstein.txt", "r") as f:
        file_content = f.read()
        print(file_content)
        print(count_words(file_content))
        print(count_letters(file_content))


main()
