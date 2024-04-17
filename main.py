def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(num_of_words(file_contents))
        print_letter_occurances(letter_occurances(file_contents))


def num_of_words(str):
    return len(str.split())


def letter_occurances(str):
    count = {}
    for char in str:
        lower_char = char.lower()
        if lower_char in count:
            count[lower_char] += 1
        else:
            count[lower_char] = 1
    return count


def print_letter_occurances(count):
    for letter, occurances in count.items():
        print(f"{letter} -> {occurances}")


if __name__ == "__main__":
    main()
