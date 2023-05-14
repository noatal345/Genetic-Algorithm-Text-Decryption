# in this  file we created three fitness functions:
# 1. dictionary_fitness: search the number of word from file that appear in the dictionary
# 2. letter_frequency_fitness: compare the letter frequency of the file to the letter frequency of the english
# language.
# 3. two_letter_frequency_fitness: compare the 2 letter frequency of the file to the 2 letter frequency of the
# english language
import re
import ex2

dictionary = ex2.create_dictionary("dict.txt")
english_letter_frequency = ex2.create_dictionary("Letter_Freq.txt")
english_2letter_frequency = ex2.create_dictionary("Letter2_Freq.txt")


def dictionary_fitness(file):
    fitness = 0
    # open the file
    with open(file, 'r') as f:
        # read the file
        file = f.read().upper()
        # split the file into words by spaces and new lines
        file = re.split(r'[\n\s]', file)
        # count the number of words from the file that appear in the dictionary
        for word in file:
            if word in dictionary:
                fitness += 1

    return fitness


def letter_frequency_fitness(file):
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

    return fitness / len(english_letter_frequency)


def two_letter_frequency_fitness(file):
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

    return fitness / len(english_2letter_frequency)


print("dictionary fitness = ", dictionary_fitness("enc.txt"))
print("letter frequency fitness = ", letter_frequency_fitness("enc.txt"))
print("two letter frequency fitness = ", two_letter_frequency_fitness("enc.txt"))
