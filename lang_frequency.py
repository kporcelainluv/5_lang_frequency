import re
from collections import Counter


def load_data_from_file():
    with open(input(), "r", encoding="utf8") as f:
        text = f.readlines()
        return text


def lowercase_split_strip_file(text):
    text = str(text).strip().lower()
    text_after_formatting = re.findall(r'\w+', text)
    for words in range(text_after_formatting.count("n")):
        if "n" in text_after_formatting:
            text_after_formatting.remove("n")
    return text_after_formatting


def get_ten_frequent_words(text):
    text_to_list = list(lowercase_split_strip_file(text))
    dict_of_words = Counter(text_to_list)
    return Counter(dict_of_words).most_common(10)


def print_list_of_frequent_words_in_column(list_of_frequent_words):
    for word in list_of_frequent_words:
        print(word[0], "-", word[1])


if __name__ == '__main__':
    print(print_list_of_frequent_words_in_column(get_ten_frequent_words(load_data_from_file())), sep="\n")
