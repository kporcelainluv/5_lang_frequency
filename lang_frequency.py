import re
from collections import Counter
import sys


def load_data(filepath):
    with open(filepath, "r", encoding="utf8") as f:
        text = f.read()
    return text


def lowercases_text_and_removes_punctuation(text):
    text = text.lower()
    text_without_punctuation = re.findall(r'\w+', text)
    return text_without_punctuation


def get_ten_frequent_words(text):
    number_of_frequent_words = 10
    counter_of_words = Counter(text)
    return counter_of_words.most_common(number_of_frequent_words)


def print_list_of_frequent_words_in_column(list_of_frequent_words):
    for word, number in list_of_frequent_words:
        print(word, "-", number)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]

print_list_of_frequent_words_in_column(
    get_ten_frequent_words(lowercases_text_and_removes_punctuation(load_data(filepath))))
