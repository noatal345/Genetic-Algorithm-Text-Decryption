# in this file we will:
# 1. fix each dictionary to contain each value only once.
# 2. create mutation function that will mutate the dictionary.
import random


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
