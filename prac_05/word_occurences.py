def main():
    word_to_count = {}
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1
    for word in words:
        print("{} : {}".format(word, word_to_count[word]))


main()
