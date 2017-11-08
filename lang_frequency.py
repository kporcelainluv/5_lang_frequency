import re
from collections import Counter
import sys


def load_data(filepath):
    with open(filepath, "r", encoding="utf8") as input_file:
        text = input_file.read()
    return text


def split_text_remove_punctuation(text):
    text_without_punctuation = re.findall(r'\w+', text.lower())
    return text_without_punctuation


def get_frequent_words(list_of_words):
    number_of_frequent_words = 10
    counter_of_words = Counter(list_of_words)
    return counter_of_words.most_common(number_of_frequent_words)


def print_frequent_words_in_column(frequent_words):
    for word, number in frequent_words:
        print(word, "-", number)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    print_frequent_words_in_column(get_frequent_words(split_text_remove_punctuation(load_data(filepath))))
