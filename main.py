def main():
    book = read_book()
    letters_count = count_letters(book)
    print_letters_count(letters_count)


def read_book():
    file_contents = "No book read"
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    if (not text):
        raise Exception("no text provided")
    
    return len(text.split())
        
def count_letters(text):
    if (not text):
        raise Exception("no text provided")
    
    letters_counter = {}

    for letter in text:
        small_letter = letter.lower()
        if (small_letter in letters_counter):
            letters_counter[small_letter] += 1
        else:
            letters_counter[small_letter] = 1

    return letters_counter

def print_letters_count(letters_count):
    letters = []

    for char in letters_count:
       if (char.isalpha()):
           letter_data = {"letter": char, "num": letters_count[char]}
           letters.append(letter_data)

    letters.sort(key=sort_on)

    for row in letters:
        print(f"The '{row["letter"]}' character was found {row["num"]} times")


    # A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["letter"]

# vehicles = [
#     {"name": "car", "num": 7},
#     {"name": "plane", "num": 10},
#     {"name": "boat", "num": 2}
# ]
# vehicles.sort(reverse=True, key=sort_on)
# print(vehicles)


main()