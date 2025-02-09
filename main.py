def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    character_count = get_num_characters(text)

    sorted_list = convert_to_sorted_list(character_count)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def sort_on(dict):
    return dict["num"]

def convert_to_sorted_list(dict):
    sorted_list = []
    for item in dict.items():
        sorted_list.append({"char": item[0], "num": item[1]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_num_characters(text):
    character_count = {}

    for character in text:
        character_lower = character.lower()
        if character_lower in character_count:
            character_count[character_lower] += 1
        else:
            character_count[character_lower] = 1

    return character_count


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()