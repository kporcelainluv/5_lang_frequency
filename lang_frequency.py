import re
import sys
from collections import Counter

filename = ""

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]


def load_data_lowercase_remove_punctuation():
    with open(filename, "r", encoding="utf8") as f:
        text = f.read().lower()
    text_without_punctuation = re.findall(r'\w+', text)
    return text_without_punctuation


def get_ten_frequent_words(text):
    number_of_frequent_words = 10
    counter_of_words = Counter(text)
    return counter_of_words.most_common(number_of_frequent_words)


def print_list_of_frequent_words_in_column(list_of_frequent_words):
    for word, number in list_of_frequent_words:
        print(word, "-", number)


print(print_list_of_frequent_words_in_column(get_ten_frequent_words(load_data_lowercase_remove_punctuation())),
      sep="\n")
