# This is the main program
# This program receives aan encoded txt file and decodes the file content using a genetic algorithm.
# the program creates 2 new files:
# 1. plain.txt an encrypted txt file of the original encoded file.
# 2. perm.txt which will contain its permutation.

from generation_functions import *
from general import *


def start(encoded_file, common_words_set, abc_dictionary, number_of_strings):
    # save the number of words and chars from the encoded file into parameters
    num_of_words, num_of_chars = count_words(encoded_file)
    # save the characters frequencies in dictionaries
    english_2letter_frequency = create_dictionary("Letter2_Freq.txt")
    english_letter_frequency = create_dictionary("Letter_Freq.txt")
    # create a set of legal characters in the english language
    # abc_dictionary = {'A', 'B', 'C'}
    # create the first generation
    generation_lst = init_first_generation(number_of_strings, abc_dictionary)
    # check if the fitness is 0 before starting the loop
    # todo - delete
    # for g in generation_lst:
    #     fitness = overall_fitness(g, encoded_file, num_of_words, common_words_set, english_letter_frequency,
    #                               english_2letter_frequency)
    #     if fitness == 0.0:
    #         print("The fitness is: ", fitness)
    #         print("The string is: ", g)
    #         return g
    # continue to the next generation
    count_lest_best = 0
    count_num_of_generations = 0
    # while the fitness is not 0
    best_fitness = float("inf")
    best_string_index = 0
    next_gen_flag = True
    mutation_num = 5
    while next_gen_flag:
        # create a new generation
        new_generation_lst = generate_next_generation(generation_lst, encoded_file, num_of_words, abc_dictionary,
                                                      common_words_set, english_letter_frequency,
                                                      english_2letter_frequency)
        count_num_of_generations += 1
        generation_lst = []
        for d in new_generation_lst:
            fitness = overall_fitness(d, encoded_file, num_of_words, common_words_set, english_letter_frequency,
                                      english_2letter_frequency)
            if fitness == best_fitness:
                count_lest_best += 1
            if fitness < best_fitness:
                best_fitness = fitness
                count_lest_best = 0
                best_string_index = new_generation_lst.index(d)
            if fitness == 0.0:
                next_gen_flag = False
                generation_lst = new_generation_lst
                print("break")
                break
            # if the best string is the same for 15 generations, increase the mutation number
            if count_lest_best % 15 == 0:
                mutation_num += 5
            # continue to the next generation
            # fix permutations
            fixed_dict = fix_permutation_dict(d, abc_dictionary)
            # mutate each dictionary in the generation
            fixed_dict = mutate_permutation_dict(fixed_dict, mutation_num)
            generation_lst.append(fixed_dict)
        print("generation number " + str(count_num_of_generations) + " best fitness is: " + str(best_fitness))
        print("best string is: " + str(generation_lst[best_string_index]))

    return generation_lst[best_string_index]


def write_permutation_to_file(perm, filename):
    # create a file named perm.txt and write the permutation to it
    with open(filename, "w") as f:
        for key, value in perm.items():
            f.write(key + "\t" + value + "\n")


def write_decoded_text_to_file(perm, encoded_file, filename):
    # create a file named plain.txt and write the decoded text to it
    with open(filename, "w") as f:
        with open(encoded_file, "r") as e:
            for line in e:
                for char in line:
                    if char in perm:
                        f.write(perm[char])
                    else:
                        f.write(char)


def main():
    # todo delete example
    # encoded_file = "test.txt"
    # common_words_set = create_english_set("new_dict.txt")
    # abc_dictionary = {'A', 'B', 'C'}
    # define the number of strings in each generation
    number_of_strings = 5

    # define parameters:
    encoded_file = "enc.txt"
    common_words_set = create_english_set("dict.txt")
    abc_dictionary = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'k', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                          'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    # define the number of strings in each generation
    number_of_strings = 500

    # start the genetic algorithm
    perm = start(encoded_file, common_words_set, abc_dictionary, number_of_strings)
    # create a file named perm.txt and write the permutation to it
    write_permutation_to_file(perm, "perm.txt")
    # create a file named plain.txt and write the decoded text to it
    write_decoded_text_to_file(perm, encoded_file, "plain.txt")


if __name__ == '__main__':
    main()