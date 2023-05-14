from random import random
import random


def create_english_dictionary(filename):
    # create a hash set
    english_dict = set()
    # open filename and append each value in each row to the english common_words_dictionary.
    with open(filename) as f:
        for line in f:
            english_dict.add(line.strip())
    # close file
    f.close()
    return english_dict


# This function receives a path to a txt file as argument.
# The function reads the file and creates a common_words_dictionary from the file.
# The function returns the new common_words_dictionary where the key is the first word and the value is the second of each row.
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
            # add the key and value to the common_words_dictionary.
            new_dict[key] = value
    f.close()
    return new_dict


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
    print("total =", total_chars)
    print("special =", special_char)
    #close file
    f.close()
    return numer_of_words, number_of_char


# def init_first_generation(num_of_strings, length, legal_characters):
#     # create a list of strings
#     list_of_strings = []
#
#     # create num_of_strings strings with length characters each of permutations of legal_characters
#     for i in range(num_of_strings):
#         new_string = ""
#         for j in range(length):
#             # choose a random character from legal_characters
#             char = random.choice(legal_characters)
#             new_string += char
#
#



# the main program
# create a common_words_dictionary of english words according to the common_words_dictionary file.
english_dict = create_english_dictionary("dict.txt")
num_of_words, num_of_chars = count_words("enc.txt")
print("number of chars = ", num_of_chars)
print("number of words = ", num_of_words)
a = create_dictionary("Letter2_Freq.txt")
b = create_dictionary("Letter_Freq.txt")
print("len(a)")
print(len(a))
print("len(b)")
print(len(b))
print(a.items())
print(b.items())



abc_dictionary = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'k', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z'}
number_of_strings = 32
length_of_string = 26
# init_first_generation(number_of_strings, length_of_string, abc_dictionary)