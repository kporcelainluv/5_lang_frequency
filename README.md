# Frequency Analysis of Words

This is the library that counts first 10 frequent words from file

# How to use

Functions in the library:

-- load_data_from_file()
 
* input: name of the txt file
* returns text from input

-- lowercase_split_strip_file(text)

* input: text
* returns: stripped, splited text without punctuation marks. Also removes "/n".

-- get_ten_frequent_words(text)

* input: text
* returns: a dictionary of 10 most frequent words from the file

-- print_list_of_frequent_words_in_column(list_of_frequent_words):

* input: list_of_frequent_words
* prints: paired key and value from dictionary in a column
* returns: none

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
