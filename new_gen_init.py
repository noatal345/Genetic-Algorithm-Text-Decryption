# in this file we will:
# 1. fix each dictionary to contain each value only once.
# 2. create mutation function that will mutate the dictionary.
import random


def fix_permutation_dict(permutation_dict):
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
    for i in range(num_of_mutations):
        # randomly choose two keys from the dictionary
        keys = list(permutation_dict.keys())
        key1 = random.choice(keys)
        key2 = random.choice(keys)
        # Swap the values of the two keys
        permutation_dict[key1], permutation_dict[key2] = permutation_dict[key2], permutation_dict[key1]

    return permutation_dict
