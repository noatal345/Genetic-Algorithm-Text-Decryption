# This file contains three fitness functions:
# 1. dictionary_fitness: search the number of word from file that appear in the common_words_dictionary
# 2. letter_frequency_fitness: compare the letter frequency of the file to the letter frequency of the english
# language.
# 3. two_letter_frequency_fitness: compare the 2 letter frequency of the file to the 2 letter frequency of the
# english language
import os

from general import count_words, create_english_set, create_dictionary


# this function will take the original encrypted file and an optional_alphabet_dictionary -
# a permutation of the alphabet and will create a new file with the letters permuted
# according to the optional_alphabet_dictionary.
def permute_file(file, optional_alphabet_dictionary):
    # open the file
    with open(file, 'r') as f:
        # read the file
        file = f.read().upper()
        # create a new file
        new_file = open("decrypted_file.txt", "w")
        # for each letter in the file, if the letter is in the optinal_alphabet_dictionary, replace it with
        # the value from the optional_alphabet_dictionary.
        # if the letter is not in the common_words_dictionary, leave it as is.
        for letter in file:
            if letter.isalpha():
                if letter in optional_alphabet_dictionary.keys():
                    new_file.write(optional_alphabet_dictionary[letter])
                else:
                    new_file.write(letter)
            else:
                new_file.write(letter)
    new_file.close()
    f.close()


def dictionary_fitness(file, num_of_words_in_file, common_words_set):
    fitness = 0
    with open(file, 'r') as f:
        for line in f:
            # Split each line into words and check if each word appears in the set of common words
            words = line.upper().strip().split()
            for word in words:
                if word in common_words_set:
                    fitness += 1
    f.close()
    return (num_of_words_in_file - fitness) / num_of_words_in_file


def letter_frequency_fitness(file, english_letter_frequency):
    fitness = 0
    file_letter_frequency = {}
    # open the file
    with open(file, 'r') as f:
        # read the file
        file = f.read().upper()
        # count the number of time each letter appears in the file
        for letter in file:
            if letter.isalpha():  # Only count letters
                if letter in file_letter_frequency:
                    file_letter_frequency[letter] += 1
                else:
                    file_letter_frequency[letter] = 1
        # normalize the counts to get frequencies
        total_count = sum(file_letter_frequency.values())
        file_letter_frequency = {letter: count / total_count for letter, count in file_letter_frequency.items()}
        # compare the letter frequency of the file to the letter frequency of the english language
        for letter in file_letter_frequency:
            if letter in english_letter_frequency:
                fitness += pow(file_letter_frequency[letter] - english_letter_frequency[letter], 2)
    f.close()

    return fitness / len(english_letter_frequency)


def two_letter_frequency_fitness(file, english_2letter_frequency):
    fitness = 0
    file_2letter_frequency = {}
    # open the file
    with open(file, 'r') as f:
        # read the file
        file = f.read().upper()
        # count the number of time each letter appears in the file
        for i in range(len(file) - 1):
            two_letter = file[i:i + 2]
            if two_letter.isalpha():
                if two_letter in file_2letter_frequency:
                    file_2letter_frequency[two_letter] += 1
                else:
                    file_2letter_frequency[two_letter] = 1
        # normalize the counts to get frequencies
        total_count = sum(file_2letter_frequency.values())
        file_2letter_frequency = {two_letter: count / total_count for two_letter, count in
                                  file_2letter_frequency.items()}
        # compare the letter frequency of the file to the letter frequency of the english language
        for two_letter in file_2letter_frequency:
            if two_letter in english_2letter_frequency:
                fitness += pow(file_2letter_frequency[two_letter] - english_2letter_frequency[two_letter], 2)
    f.close()

    return fitness / len(english_2letter_frequency)


def overall_fitness(optional_alphabet_dictionary, file, num_of_words_in_file, common_words_set,
                    english_letter_frequency, english_2letter_frequency):
    permute_file(file, optional_alphabet_dictionary)
    words_freq = dictionary_fitness("decrypted_file.txt", num_of_words_in_file, common_words_set)
    letters_freq = letter_frequency_fitness("decrypted_file.txt", english_letter_frequency)
    two_letters_freq = two_letter_frequency_fitness("decrypted_file.txt", english_2letter_frequency)
    if words_freq == 0.0 or words_freq == 0:
        os.remove("decrypted_file.txt")
        print("if words_freq == 0")
        return 0
    else:
        w1, w2, w3 = 0.5, 0.25, 0.25
        fitness = w1 * words_freq + w2 * letters_freq + w3 * two_letters_freq
        # remove the decrypted file
        os.remove("decrypted_file.txt")
    return fitness
