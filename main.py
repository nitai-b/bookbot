def get_book_contents(path):
    with open(path) as f:
        return f.read()

def get_word_count(contents):
    return len(contents.split(" "))

def main() -> int:
    contents = get_book_contents("./frankenstein.txt")
    print(contents)

    word_count = get_word_count(contents)
    print(word_count)

    return 0

main()
