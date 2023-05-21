import random
import math
from config import ELITE_SIZE, MUTATION_RATE, ABC_SET


def init_first_generation(num_of_strings, legal_characters=ABC_SET):
    # Create a list of strings dictionary's - The generation to return
    list_of_strings = []
    # Cope the legal_characters to a new set
    characters_left = set(legal_characters)
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
        # Reset the characters_left set for the next string
        characters_left = set(legal_characters)
    # return the list of strings
    return list_of_strings


def check_convergence(generation_lst, fitness_lst):
    # check for convergence
    # sort curr_gen by fitness and take the first 0.05 of the generation
    generation_lst = [x for _, x in sorted(zip(fitness_lst, generation_lst), key=lambda pair: pair[0])][
                     :int(0.333 * len(generation_lst))]
    # convert the dictionarys in the generation list to strings
    new_generation_lst = []
    for string in generation_lst:
        new_string = ""
        for letter in ABC_SET:
            new_string += string[letter]
        new_generation_lst.append(new_string)
    # check if all the strings in the new generation are the same
    if len(set(new_generation_lst)) == 1:
        return True
    return False


def fix_permutation_dict(permutation_dict):
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
                available_values = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ') - set(permutation_dict.values())
                if len(available_values) > 0:
                    new_value = available_values.pop()
                    permutation_dict[key] = new_value
                    values.add(new_value)
                else:
                    # There are no more available values to use, so we can't fix the dictionary
                    return None

    return permutation_dict


def mutate_permutation_dict(permutation_dict, mutation_rate=MUTATION_RATE):
    permutation_dict_copy = permutation_dict.copy()
    for key1 in permutation_dict_copy.keys():
        if random.random() < mutation_rate:
            key2 = random.choice(list(permutation_dict_copy.keys()))
            # Swap the values of the two keys
            permutation_dict_copy[key1], permutation_dict_copy[key2] = permutation_dict_copy[key2], permutation_dict_copy[key1]

    return permutation_dict_copy


def generate_initial_guesses(num_guesses, fitness):
    ciphertext_frequencies = fitness.file_letter_frequency
    plaintext_frequencies = fitness.english_letter_frequency

    guesses_list = []
    ciphertext_letters = list(ciphertext_frequencies.keys())
    plaintext_letters = list(plaintext_frequencies.keys())
    # Repeat the process for the specified number of guesses
    for _ in range(num_guesses):
        guesses = {}
        remaining_plaintext_letters = plaintext_letters[:]
        # Sort the ciphertext letters based on their frequencies in descending order
        sorted_ciphertext_letters = sorted(ciphertext_letters, key=lambda x: ciphertext_frequencies[x], reverse=True)
        # Sort the plaintext letters based on their frequencies in descending order
        sorted_plaintext_letters = sorted(remaining_plaintext_letters, key=lambda x: plaintext_frequencies[x],
                                          reverse=True)
        # Map the most frequent letters in the ciphertext to the most frequent letters in the plaintext
        for i in range(len(sorted_ciphertext_letters)):
            ciphertext_letter = sorted_ciphertext_letters[i]
            # Randomly select a remaining plaintext letter from the top ranked options
            num_top_options = min(i + 1, len(sorted_plaintext_letters))
            random_plaintext_letter = random.choice(sorted_plaintext_letters[:num_top_options])
            sorted_plaintext_letters.remove(random_plaintext_letter)
            guesses[ciphertext_letter] = random_plaintext_letter
            remaining_plaintext_letters.remove(random_plaintext_letter)
        guesses_list.append(guesses)
    return guesses_list


def calc_probabilities(fitness_lst):
    # get the index of the elite strings
    elite_index = sorted(range(len(fitness_lst)), key=lambda i: fitness_lst[i])[:ELITE_SIZE]
    # invert the fitness list
    inverted_fitness_lst = [1 / fitness for fitness in fitness_lst]
    # softmax
    # calc exp for each inverted fitness
    exp_inverted_fitness_lst = [math.exp(inv_fitness) for inv_fitness in inverted_fitness_lst]
    # calc sum of exp inverted fitness
    sum_of_exp_inverted_fitness = sum(exp_inverted_fitness_lst)
    # calc probabilities
    probabilities = [exp_inv_fitness / sum_of_exp_inverted_fitness for exp_inv_fitness in exp_inverted_fitness_lst]

    return probabilities, elite_index


def generate_next_generation(generation_lst, legal_characters, fitness_lst):
    # create a new generation list.
    new_generation_lst = []
    # calculate probabilities for each string in the generation list
    probabilities, bests_indexes = calc_probabilities(fitness_lst)
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
        # fix the new string
        new_string = fix_permutation_dict(new_string)
        # mutate the new string
        new_string = mutate_permutation_dict(new_string)
        # add the new string to the new generation
        new_generation_lst.append(new_string)
    return new_generation_lst


def local_optimization(perm):
    pass

