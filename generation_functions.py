# This file contains two functions:
# 1. receives a dictionary and fix it to contain each english character exactly.
# 2. mutation function - mutate the dictionary.
import math
import random

from numpy import mean

from fitness import *
import numpy as np


def fix_permutation_dict(permutation_dict, legal_characters):
    """
    The fix_permutation_dict function takes a dictionary that is supposed to be a permutation of the alphabet and
    attempts to fix it if it is not. It does this by removing duplicate values from the dictionary, replacing them with
    values that are not already in use. If there are no more available values, then we cannot fix the dictionary.

    :param permutation_dict: A dictionary that is supposed to be a permutation of the alphabet
    :return: A dictionary that is a valid permutation
    """
    values = set()
    duplicates_keys = set()

    for key, value in permutation_dict.items():
        if value in values:
            duplicates_keys.add(key)
        else:
            values.add(value)

    if len(values) != 26:
        # The dictionary is not a valid permutation, so attempt to fix it by removing any duplicate values
        for key, value in permutation_dict.items():
            if key in duplicates_keys:
                # Find all the values that are not in the dictionary
                # available_values = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ') - set(permutation_dict.values())
                available_values = set(legal_characters) - set(permutation_dict.values())
                if len(available_values) > 0:
                    new_value = available_values.pop()
                    permutation_dict[key] = new_value
                    values.add(new_value)
                else:
                    # There are no more available values to use, so we can't fix the dictionary
                    return None

    return permutation_dict


def mutate_permutation_dict(permutation_dict, num_of_mutations):
    """
    The mutate_permutation_dict function takes in a permutation dictionary and the number of mutations to be made.
    It then randomly chooses two keys from the dictionary, swaps their values, and returns the mutated permutation
    dictionary.

    :param permutation_dict: A dictionary that is a permutation of the alphabet
    :param num_of_mutations: Determine how many times the values of two keys in the dictionary are swapped
    :return: A dictionary that is a permutation of the alphabet after being mutated
    """
    for i in range(num_of_mutations):
        # randomly choose two keys from the dictionary
        keys = list(permutation_dict.keys())
        key1 = random.choice(keys)
        key2 = random.choice(keys)
        # Swap the values of the two keys
        permutation_dict[key1], permutation_dict[key2] = permutation_dict[key2], permutation_dict[key1]

    return permutation_dict


def init_first_generation(num_of_strings, legal_characters, encoded_file, num_of_words_in_file, common_words_set,
                          english_letter_frequency, english_2letter_frequency):
    # Create a list of strings dictionary's - The generation to return
    list_of_strings = []
    # Cope the legal_characters to a new set
    characters_left = set(legal_characters)
    # Create a list of fitness values
    fitness_lst = []
    # create num_of_strings number of strings with the length of length each of legal_characters permutations
    for i in range(num_of_strings):
        # create a new string dictionary
        new_string = {}
        for j in legal_characters:
            # choose a random character from legal_characters
            char = random.choice(list(characters_left))
            # add the character to the new string
            new_string[j] = char
            # remove the character from the set of characters left to choose from
            characters_left.remove(char)
        # add the new string to the list of strings
        list_of_strings.append(new_string)
        # calculate the fitness of the string
        fitness, words_freq, letters_freq, two_letters_freq = overall_fitness(new_string, encoded_file, num_of_words_in_file,
                                                              common_words_set, english_letter_frequency,
                                                              english_2letter_frequency)
        # add the fitness to the fitness list
        fitness_lst.append(fitness)
        # Reset the characters_left set for the next string
        characters_left = set(legal_characters)
    # return the list of strings
    return list_of_strings, fitness_lst


# # This function receives a number of strings and a set of legal characters.
# # The function returns a list of strings where each string is a dictionary,
# # presenting the permutation of the legal characters without repeats.
# def init_first_generation(num_of_strings, legal_characters, encoded_file, num_of_words_in_file, common_words_set,
#                           english_letter_frequency, english_2letter_frequency):
#     l = float("inf")
#     l2 = float("inf")
#     counter = 0
#     while l > 0.0022 or l2 > 0.0000152:
#         print("init_first_generation", counter)
#         counter += 1
#         fitness_lst = []
#         l_lst = []
#         l2_lst = []
#         # Create a list of strings dictionary's - The generation to return
#         list_of_strings = []
#         # Cope the legal_characters to a new set
#         characters_left = set(legal_characters)
#         # create num_of_strings number of strings with the length of length each of legal_characters permutations
#         for i in range(num_of_strings):
#             # create a new string dictionary
#             new_string = {}
#             for j in legal_characters:
#                 # choose a random character from legal_characters
#                 char = random.choice(list(characters_left))
#                 # add the character to the new string
#                 new_string[j] = char
#                 # remove the character from the set of characters left to choose from
#                 characters_left.remove(char)
#             # add the new string to the list of strings
#             list_of_strings.append(new_string)
#             # calculate the fitness of the string
#             fitness, words_freq, letters_freq, two_letters_freq = overall_fitness(new_string, encoded_file, num_of_words_in_file,
#                                                                   common_words_set, english_letter_frequency,
#                                                                   english_2letter_frequency)
#             l_lst.append(letters_freq)
#             l2_lst.append(two_letters_freq)
#             fitness_lst.append(fitness)
#             # Reset the characters_left set for the next string
#             characters_left = set(legal_characters)
#         l = mean(l_lst)
#         l2 = mean(l2_lst)
#         print("l mean: ", l)
#         print("l2 mean: ", l2)
#         if l < 0.0022:
#             print("l is good")
#         if l2 < 0.000015:
#             print("l2 is good")
#     # return the list of strings
#     return list_of_strings, fitness_lst


def calc_probabilities(generation_lst, fitness_lst):
    # number of string to pass to the next generation as is no cross over
    num_of_bests = len(generation_lst) * 2 // 100
    total = sum(fitness_lst)
    # create a list of probabilities for each string in the generation
    probabilities = []
    for f in fitness_lst:
        if total != 0:
            p = 1 - (f / total)
        else:
            p = 1
        probabilities.append(p)
    # find the best "num of bests" strings of the generation
    bests = sorted(range(len(fitness_lst)), key=lambda k: fitness_lst[k])[:num_of_bests]
    # # apply min max normalization on the probabilities
    # if (max(probabilities) - min(probabilities)) != 0:
    #     probabilities = [(p - min(probabilities)) / (max(probabilities) - min(probabilities)) for p in probabilities]
    return probabilities, bests


# This function receives a list of strings which is the current generation.
# The function returns a new list of strings where each string is a dictionary,
# presenting the permutation of the legal characters without repeats.
def generate_next_generation(generation_lst, encoded_file, num_of_words, legal_characters, common_words_set,
                             english_letter_frequency, english_2letter_frequency, fitness_lst):
    # create a new generation list.
    new_generation_lst = []
    # calculate probabilities for each string in the generation list
    probabilities, bests_indexes = calc_probabilities(generation_lst, fitness_lst)
    #todo ?
    if sum(probabilities) <= 0:
        return generation_lst
    # convert legal characters to a list
    legal_characters_lst = list(legal_characters)
    # sample 2 strings and a crossover point for range (len(generation_strings)) times
    # create a new string from the 2 strings and the crossover point
    # add the new string to the new generation
    for i in range(len(generation_lst)):
        if i in bests_indexes:
            new_generation_lst.append(generation_lst[i])
            continue
        # choose 2 random strings from the generation according to the probabilities
        first_str, second_str = random.choices(generation_lst, weights=probabilities, k=2)
        # choose a random number from 0 to 25 - the crossover position
        crossover_point = random.randint(0, len(legal_characters_lst) - 1)
        # create the new string
        new_string = {}
        for j in range(crossover_point):
            new_string[legal_characters_lst[j]] = first_str[legal_characters_lst[j]]
        for j in range(crossover_point, len(legal_characters_lst)):
            new_string[legal_characters_lst[j]] = second_str[legal_characters_lst[j]]
        # add the new string to the new generation
        new_generation_lst.append(new_string)
    return new_generation_lst, bests_indexes

