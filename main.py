def count_words(text):
    return len(text.split())


def count_letters(text):
    counted = {}
    for letter in text:
        key = letter.lower()
        val = counted.get(key, 0) + 1
        counted[key] = val
    return counted

def sort_on(dict):
    return dict["num"]

def sorted_count_letter(letter_count_dict: dict):
  letter_count_list = []
  for letter, count in letter_count_dict.items():
    if not letter.isalpha():
        continue
    letter_count_list.append({"letter": letter, "num": count})
  letter_count_list.sort(reverse=True, key=sort_on)
  return letter_count_list



def print_report(text, title):
    word_count = count_words(text)
    letter_count_dict = count_letters(text)
    letter_count_list = sorted_count_letter(letter_count_dict)
    print(f"--- Begin report of {title} ---")
    print(f"{word_count} words found in the document")
    print("\n\n")
    for letter in letter_count_list:
        print(f"The '{letter["letter"]}' character was found {letter["num"]} times")
    print("--- End report ---")


def main():
    file = "books/frankenstein.txt"
    with open(file, "r") as f:
        file_content = f.read()
        print_report(file_content, file)


main()
