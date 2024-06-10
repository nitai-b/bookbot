def get_book_contents(path):
    with open(path) as f:
        return f.read()

def get_word_count(contents):
    return len(contents.lower().split(" "))

def get_character_count(contents):
    contents = contents.lower().replace("\n", " ").replace(" ", "")

    char_count = {}
    for letter in contents:
        if letter.isalpha():
            if letter in char_count.keys():
                    num = char_count.get(letter)
                    char_count[letter] = num + 1
            else:
                char_count[letter] = 1

    char_count_expanded = []
    count = 0
    for letter in char_count.keys():
        x = {}
        x["name"] = letter
        x["occurances"] = char_count.get(letter)
        char_count_expanded.insert(count, x)
        ++count

    return char_count, char_count_expanded


def main() -> int:
    contents = get_book_contents("./frankenstein.txt")
    print(f"Contents | {contents}")

    word_count = get_word_count(contents)
    print(f"Word Count | {word_count}")

    character_count, char_count_exp = get_character_count(contents)
    print(f"Character Count | {character_count} | {char_count_exp}")

    # A function that takes a dictionary and returns the value of the "num" key
    # This is how the `.sort()` method knows how to sort the list of dictionaries
    def sort_on(dict):
        return dict["occurances"]

    char_count_exp.sort(key=sort_on, reverse=True)

    for character in char_count_exp:
        print(f"The '{character['name']}' character was found '{character['occurances']}' times.")

    return 0

main()
