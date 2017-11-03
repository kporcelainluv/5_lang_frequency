import re
from collections import Counter
import sys


def load_data(filepath):
    with open(filepath, "r", encoding="utf8") as file:
        text = file.read()
    return text


def remove_punctuation(text):
    text_without_punctuation = re.findall(r'\w+', text.lower())
    return text_without_punctuation


def get_frequent_words(text):
    number_of_frequent_words = 10
    counter_of_words = Counter(text)
    return counter_of_words.most_common(number_of_frequent_words)


def print_list_of_frequent_words_in_column(list_of_frequent_words):
    for word, number in list_of_frequent_words:
        print(word, "-", number)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]

print_list_of_frequent_words_in_column(get_frequent_words(remove_punctuation(load_data(filepath))))
