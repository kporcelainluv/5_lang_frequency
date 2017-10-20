# Frequency Analysis of Words

This is the library that counts first 10 frequent words from file

# How to use

Functions in the library:

-- load_data
 
* input: path to the file
* returns text from input

-- get_most_frequent_words

* input: text
* returns: sorted list of 10 most frequent words

# How to launch

Example:

```
from lang_frequency import get_most_frequent_words
  mylist = get_most_frequent_words(name of file in the directory)
```  
Script requires installed Python interpretator, version 3.5

How to launch on Linux:
```
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```
The launch on Windows can be done in similar way.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
