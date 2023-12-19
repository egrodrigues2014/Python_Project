# twttr

def main():
    phrase = input("Input:")
    message = shorten(phrase)
    print("Output:", message)

def shorten(word):
    word_without_vowels = ""
    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            word_without_vowels += char
    return word_without_vowels

if __name__ == "__main__":
    main()
