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

    # create the first generation
    generation_lst = init_first_generation(number_of_strings, abc_dictionary)
    fitness_lst = []
    # calculate the first fitness list
    for d in generation_lst:
        fitness_lst.append(overall_fitness(d, encoded_file, num_of_words, common_words_set, english_letter_frequency,
                                           english_2letter_frequency))
    # initialize variables
    count_num_of_generations = 0
    best_fitness = float("inf")
    best_index = 0
    count_last_best = 0
    mutation_num = 5
    count_bigger = 0
    # run the algorithm until convergence
    while 1:
        # create a new generation
        new_generation_lst, bests_indexes = generate_next_generation(generation_lst, encoded_file, num_of_words, abc_dictionary,
                                                      common_words_set, english_letter_frequency,
                                                      english_2letter_frequency, fitness_lst)
        # initialize variables for the new generation
        gen_best_fitness = float("inf")
        gen_best_index = 0
        count_num_of_generations += 1
        generation_lst = []
        # choose 0.2*number of strings random numbers from number_of_strings-best_indexes
        legal_range = [x for x in range(number_of_strings) if x not in bests_indexes]
        indexes_to_mutate = random.sample(legal_range, int(len(legal_range) * 0.3))
        fitness_lst = []

        for d in new_generation_lst:
            # fix the new string permutations
            fixed_dict = fix_permutation_dict(d, abc_dictionary)
            # mutate the new string
            current_index = new_generation_lst.index(d)
            if current_index in indexes_to_mutate:
                fixed_dict = mutate_permutation_dict(fixed_dict, mutation_num)
            # add the new string to the new generation
            generation_lst.append(fixed_dict)
            # calculate the fitness of each string in the generation
            fitness = overall_fitness(d, encoded_file, num_of_words, common_words_set, english_letter_frequency,
                                      english_2letter_frequency)
            fitness_lst.append(fitness)
            if fitness < gen_best_fitness:
                gen_best_fitness = fitness
                gen_best_index = new_generation_lst.index(d)
        # at the end of each generation save the best permutation so far.
        # and count the number of generations with the same best string
        if gen_best_fitness < best_fitness:
            best_fitness = gen_best_fitness
            best_index = gen_best_index
            count_last_best = 0
            count_bigger = 0
            mutation_num = 5
        elif gen_best_fitness == best_fitness:
            count_last_best += 1
        elif gen_best_fitness > best_fitness:
            count_bigger += 1
            mutation_num = 5
        # if the best string is the same for 10 generations, increase the mutation number
        if (count_last_best > 0 and count_last_best % 15 == 0) or count_bigger > 20:
            mutation_num += 2
            print("count_bigger", count_bigger)
            print("mutation number is :", mutation_num)
        # if the best string is the same for 20 generations after adding more mutations, stop the loop
        if count_last_best > 0 and count_last_best % 200 == 0:
            print("break while loop")
            break
        print("count_last_best is: " + str(count_last_best))
        print("generation number " + str(count_num_of_generations) + " best fitness is: " + str(best_fitness))
        print("best string is: " + str(generation_lst[best_index]))
    return generation_lst[best_index]


def write_permutation_to_file(perm):
    # create a file named perm.txt and write the permutation to it
    with open("perm.txt", "w") as f:
        for key, value in perm.items():
            f.write(key + "\t" + value + "\n")
    f.close()
    return f


def write_decoded_text_to_file(perm, encoded_file):
    # open the file
    with open(encoded_file, 'r') as f:
        # read the file
        file = f.read().upper()
        # create a new file
        new_file = open("plain.txt", "w")
        # for each letter in the encoded file, if the letter is in the perm dictionary, replace it with
        # the value from the perm dictionary.
        # if the letter is not in the perm dictionary, leave it as is.
        for letter in file:
            if letter.isalpha():
                if letter in perm.keys():
                    new_file.write(perm[letter])
                else:
                    new_file.write(letter)
            else:
                new_file.write(letter)


def main():
    # todo delete example
    # encoded_file = "test.txt"
    # common_words_set = create_english_set("new_dict.txt")
    # abc_dictionary = {'A', 'B', 'C'}
    # # define the number of strings in each generation
    # number_of_strings = 6

    # define parameters:
    encoded_file = "enc.txt"
    common_words_set = create_english_set("dict.txt")
    abc_dictionary = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'k', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                      'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    # define the number of strings in each generation
    number_of_strings = 250

    # start the genetic algorithm
    perm = start(encoded_file, common_words_set, abc_dictionary, number_of_strings)
    # create a file named perm.txt and write the permutation to it
    write_permutation_to_file(perm)
    # create a file named plain.txt and write the decoded text to it
    write_decoded_text_to_file(perm, encoded_file)
    # print thr permutation from the perm.txt file
    with open("perm.txt", 'r') as f:
        file = f.read().upper()
        print(file)
    f.close()

    # read the decoded text from the file plain.txt
    with open("plain.txt", 'r') as f:
        file = f.read().upper()
        print(file)
    f.close()


if __name__ == '__main__':
    main()