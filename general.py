# This file contains general functions that are used in the to initiate the main.py file.

# convert the dict.txt file to a set of words.
def create_english_set(filename):
    # create a hash set
    english_set = set()
    # open filename and append each value in each row to the english dictionary.
    with open(filename) as f:
        for line in f:
            english_set.add(line.upper().strip())
    # close file
    f.close()
    return english_set


# This function receives a path to a txt file as argument.
# The function reads the file and creates a dictionary from the file.
# The function returns the new dictionary where the key is the first word and the value is the second of each row.
def create_dictionary(filename):
    new_dict = {}
    # open the filename and read each line.
    with open(filename) as f:
        for line in f:
            if line == "\t\n" or line == "\n" or line == "\t":
                break
            # if the line is empty or the line doesn't contain a "\t" char continue to the next line.
            if "\t" not in line:
                continue
            # split the line to key and value according to "\t" tab space.
            value, key = line.split("\t")
            # remove the "\n" from the key.
            key = key.strip()
            # convert the value to float.
            value = float(value)
            # add the key and value to the dictionary.
            new_dict[key] = value
    f.close()
    return new_dict


# This function receives a path to a txt file as argument and return the number of characters and words in it
def count_words(filename):
    # create a set of characters that are not part of a word.
    characters = {".", ",", " ", "\n", ";"}
    # set of word delimiters
    new_word_delimiter = {" ", "\n"}
    numer_of_words, special_char, total_chars = 0, 0, 0
    flag_word = False
    # open filename and count the number characters and the number of words in the file.
    with open(filename) as f:
        for line in f:
            for char in line:
                total_chars += 1
                if char in characters:
                    special_char += 1
                    if char in new_word_delimiter:
                        if flag_word:
                            numer_of_words += 1
                            flag_word = False
                else:
                    flag_word = True
    number_of_char = total_chars - special_char
    # close file
    f.close()
    return numer_of_words, number_of_char

