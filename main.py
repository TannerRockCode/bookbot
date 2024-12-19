def main():
    alphabet_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 
    'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
    'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    book_path = "books/frankenstein.txt"
    text = get_file_contents(book_path)
    words_count = get_word_count(text)
    print(f"Word count of book: {words_count}")
    alphabet_counted = get_alphabet_count(text, alphabet_count)
    #print(f"Alphabet Count: {alphabet_counted}")
    print_alphabet_count(alphabet_counted)


def get_word_count(text):
    words = text.split()
    return len(words)

def get_file_contents(path):
    with open(path) as f:
        return f.read()

def get_alphabet_count(text, alphabet_count):
    words = text.split()
    for word in words:
        for char in word:
            lc_char = char.lower()
            if lc_char in alphabet_count.keys():
                alphabet_count[lc_char] += 1
    return alphabet_count
            #match_alpha = alphabet_count.get(char)

def print_alphabet_count(alphabet_counted):
    for alpha in alphabet_counted:
        print(f"The '{alpha}' character was found {alphabet_counted[alpha]} times")
            




main()