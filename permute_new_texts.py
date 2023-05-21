import random
from init_varibals import ABC_SET
import Fitness_class as fit


def init_first_generation(num_of_strings, legal_characters):
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


def permute_file(optional_alphabet_dictionary, file_to_decode, decoded_file_name):
    # open the file
    with open(file_to_decode, 'r') as f:
        # read the file
        file_to_decode = f.read().upper()
        # create a new file
        new_file = open(decoded_file_name, "w")
        # for each letter in the file, if the letter is in the optinal_alphabet_dictionary, replace it with
        # the value from the optional_alphabet_dictionary.
        # if the letter is not in the optional_alphabet_dictionary, leave it as is.
        # if the char is not a letter, leave it as is.
        for letter in file_to_decode:
            if letter.isalpha():
                if letter in optional_alphabet_dictionary:
                    new_file.write(optional_alphabet_dictionary[letter].lower())
                else:
                    new_file.write(letter.lower())
            else:
                new_file.write(letter.lower())
    new_file.close()
    f.close()


permutation = init_first_generation(1, ABC_SET)[0]
file = "../../../Downloads/ביולוגיה חישובית 2/chatGPT.txt"
new_file_name = "encoded" + file

permute_file(permutation, file, new_file_name)

# creat a new file saving the permutation
abc_lst = list(ABC_SET)
abc_lst.sort()

tuple_lst = []
for letter in abc_lst:
    tuple_lst.append((permutation[letter].lower(), letter))
# sort the tuple list by the first element in the tuple
tuple_lst.sort(key=lambda x: x[0])
# save the permutation to a file
with open("correct_perm.txt", "w") as f:
    for t in tuple_lst:
        f.write(t[0] + " " + t[1] + "\n")
f.close()

# reverse the permutation
reverse_permutation = {}
for letter in abc_lst:
    reverse_permutation[permutation[letter]] = letter

# calculate the fitness of the permutation
fittness = fit.Fitness(new_file_name)
print(fittness.overall_fitness(reverse_permutation))
