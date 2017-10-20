import re


def load_data():
    filename = input("Enter path to the file: ")
    myopen = open(filename, "r", encoding="utf8")
    theText = myopen.readlines()
    return theText


def formating(text):
    text = str(text)
    text = text.lower()
    pattern = re.compile('\w+')
    text = pattern.findall(text)
    return text


def print_list(list):
    for i in list:
        print(i[0], "-", i[1])


def get_most_frequent_words(text):
    dictOfWords = dict()
    for word in formating(text):
        if word in dictOfWords:
            dictOfWords[word] += 1
        else:
            dictOfWords[word] = 1

    listOfWords = list()

    for i in dictOfWords:
        listOfWords.append((dictOfWords[i], i))

    listOfWords = sorted(listOfWords)
    listOfWords = sorted(listOfWords, key=lambda x: x[0], reverse=True)
    return (print_list(listOfWords))


print(get_most_frequent_words(load_data()), sep="\n")
