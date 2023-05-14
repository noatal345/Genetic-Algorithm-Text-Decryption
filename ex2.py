from random import random
import random


def create_english_dictionary(filename):
    # create a hash set
    english_dict = set()
    # open filename and append each value in each row to the english dictionary.
    with open(filename) as f:
        for line in f:
            english_dict.add(line.upper().strip())
    # close file
    f.close()
    return english_dict


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

# This function receives a number of strings, length of each string and a set of legal characters.
# The function returns a list of strings where each string is a permutation of the legal characters without repeats.
def init_first_generation(num_of_strings, length, legal_characters):
    # Create a list of strings - The generation to return
    list_of_strings = []
    # Cope the legal_characters to a new set
    characters_left = set(legal_characters)
    # create num_of_strings number of strings with the length of length each of legal_characters permutations
    for i in range(num_of_strings):
        new_string = ""
        for j in range(length):
            # choose a random character from legal_characters
            char = random.choice(list(characters_left))
            # add the character to the new string
            new_string += char
            # remove the character from the set of characters left to choose from
            characters_left.remove(char)
        # add the new string to the list of strings
        list_of_strings.append(new_string)
        # Reset the characters_left set for the next string
        characters_left = set(legal_characters)
    # return the list of strings
    return list_of_strings


# This is the main program
# This program receives a path to an encoded txt file as argument and decode the file content using genetic algorithm.
# the program creates 2 new files:
# plain.txt an encrypted txt file of the original encoded file.
# perm.txt which will contain its permutation.
def main():
    # create a dictionary of words according to the english dictionary file.
    english_dict = create_english_dictionary("dict.txt")
    # count the number of words and chars int the encoded file.
    num_of_words, num_of_chars = count_words("enc.txt")
    # save the characters frequencies in dictionaries
    Letter2_Freq = create_dictionary("Letter2_Freq.txt")
    Letter_Freq = create_dictionary("Letter_Freq.txt")
    # create a set of legal characters
    abc_dictionary = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'k', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    # define parameters
    number_of_strings = 32
    length_of_string = 26
    # create a list of strings - the first generation
    generation_strings = init_first_generation(number_of_strings, length_of_string, abc_dictionary)
    print(generation_strings)

if __name__ == '__main__':
    main()