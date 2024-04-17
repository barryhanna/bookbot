def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = num_of_words(file_contents)
        letters = letter_occurances(file_contents)
        total = sorted(letters.items(), key=lambda item: item[1], reverse=True)
        print_book_report("books/frankenstein.txt", words, total)


def num_of_words(str):
    return len(str.split())


def letter_occurances(str):
    count = {}
    for char in str:
        if not char.isalpha():
            continue
        lower_char = char.lower()
        if lower_char in count:
            count[lower_char] += 1
        else:
            count[lower_char] = 1
    return count


def print_book_report(file, words, character_total):
    print(f"--- Being report of {file} ---")
    print(f"{words} found in the document\n")
    for char, total in character_total:
        print(f"The '{char}' was found {total} times")
    print("--- End report ---")


def print_letter_occurances(count):
    for letter, occurances in count.items():
        print(f"{letter} -> {occurances}")


if __name__ == "__main__":
    main()
