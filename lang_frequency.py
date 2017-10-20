import re


def load_data():
    filename = input("Enter path to the file: ")
    open_text = open(filename, "r", encoding="utf8")
    formated_text = open_text.readlines()
    return formated_text


def formating(text):
    text = str(text)
    text = text.lower()
    pattern = re.compile('\w+')
    text = pattern.findall(text)
    return text


def print_list(register):
    for word in register:
        print(word[0], "-", word[1])


def get_most_frequent_words(text):
    dict_of_words = dict()
    for word in formating(text):
        if word in dict_of_words:
            dict_of_words[word] += 1
        else:
            dict_of_words[word] = 1

    register_of_words = list()

    for words in dict_of_words:
        register_of_words.append((dict_of_words[words], words))

    register_of_words = sorted(register_of_words)
    register_of_words = sorted(register_of_words, key=lambda x: x[0], reverse=True)[1:11]
    return print_list(register_of_words)


print(get_most_frequent_words(load_data()), sep="\n")
