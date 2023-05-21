from asyncio import sleep

import Fitness_class as fit
from generation_functions import *
from config import *
import sys
import tkinter as tk


def run_lamarck_algo(file_name):
    fitness = fit.Fitness(file_name)
    best_string_lst = []
    num_of_overall_generations = 0
    for j in range(NUM_OF_RUNS):
        curr_gen = generate_initial_guesses(GENERATION_SIZE, fitness)
        gen_count = 0
        best_string = ""
        best_fitness = float("inf")
        best_fitness_count = 0
        min_fitness = float("inf")
        for i in range(NUM_Of_GENERATIONS):
            gen_count += 1
            # mutate the strings in the generation
            mutate_gen = [mutate_permutation_dict(string, LAMARCK_MUTATION_RATE) for string in curr_gen]
            # calculate the fitness of each string in the generation
            mut_fitness_lst = [fitness.overall_fitness(string) for string in mutate_gen]
            cur_fitness_lst = [fitness.overall_fitness(string) for string in curr_gen]
            fitness_lst = []
            for k in range(len(mut_fitness_lst)):
                if mut_fitness_lst[k] < cur_fitness_lst[k]:
                    fitness_lst.append(mut_fitness_lst[k])
                    curr_gen[k] = mutate_gen[k]
                else:
                    fitness_lst.append(cur_fitness_lst[k])
            min_fitness = min(fitness_lst)
            best_string = curr_gen[fitness_lst.index(min_fitness)]
            if min_fitness < best_fitness:
                best_fitness = min_fitness
                best_fitness_count = 0
            elif min_fitness == best_fitness:
                best_fitness_count += 1
            else:
                best_fitness_count = 0

            if best_fitness_count > 100:
                num_of_overall_generations += gen_count
                break
            curr_gen = generate_next_generation(curr_gen, ABC_SET, fitness_lst)
            if i == NUM_Of_GENERATIONS - 1:
                num_of_overall_generations += gen_count
        best_string_lst.append((min_fitness, best_string))
    best_string_lst.sort(key=lambda x: x[0])
    best_string = best_string_lst[0][1]
    return best_string, num_of_overall_generations


def run_darwin_algo(file_name):
    fitness = fit.Fitness(file_name)
    best_string_lst = []
    num_of_overall_generations = 0
    for j in range(NUM_OF_RUNS):
        curr_gen = generate_initial_guesses(GENERATION_SIZE, fitness)
        gen_count = 0
        best_string = ""
        best_fitness = float("inf")
        best_fitness_count = 0
        min_fitness = float("inf")
        for i in range(NUM_Of_GENERATIONS):
            gen_count += 1
            # mutate the strings in the generation
            mutate_gen = [mutate_permutation_dict(string, DARVIN_MUTATION_RATE) for string in curr_gen]
            # calculate the fitness of each string in the generation
            reg_fitness_lst = [fitness.overall_fitness(string) for string in curr_gen]
            mut_fitness_lst = [fitness.overall_fitness(string) for string in mutate_gen]
            fitness_lst = [min(reg_fitness_lst[i], mut_fitness_lst[i]) for i in range(len(reg_fitness_lst))]
            min_fitness = min(fitness_lst)
            best_string = curr_gen[fitness_lst.index(min_fitness)]
            if min_fitness < best_fitness:
                best_fitness = min_fitness
                best_fitness_count = 0
            elif min_fitness == best_fitness:
                best_fitness_count += 1
            else:
                best_fitness_count = 0

            if best_fitness_count > 100:
                num_of_overall_generations += gen_count
                break
            curr_gen = generate_next_generation(curr_gen, ABC_SET, fitness_lst)
            if i == NUM_Of_GENERATIONS - 1:
                num_of_overall_generations += gen_count
        best_string_lst.append((min_fitness, best_string))
    best_string_lst.sort(key=lambda x: x[0])
    best_string = best_string_lst[0][1]
    return best_string, num_of_overall_generations


def run_regular_algo(file_name):
    fitness = fit.Fitness(file_name)
    best_string_lst = []
    num_of_overall_generations = 0
    for j in range(NUM_OF_RUNS):
        curr_gen = generate_initial_guesses(GENERATION_SIZE, fitness)
        gen_count = 0
        best_string = ""
        best_fitness = float("inf")
        best_fitness_count = 0
        min_fitness = float("inf")
        for i in range(NUM_Of_GENERATIONS):
            gen_count += 1
            # calculate the fitness of each string in the generation
            fitness_lst = [fitness.overall_fitness(string) for string in curr_gen]
            min_fitness = min(fitness_lst)
            best_string = curr_gen[fitness_lst.index(min_fitness)]
            if min_fitness < best_fitness:
                best_fitness = min_fitness
                best_fitness_count = 0
            else:
                best_fitness_count += 1

            if best_fitness_count > 100:
                num_of_overall_generations += gen_count
                break

            curr_gen = generate_next_generation(curr_gen, ABC_SET, fitness_lst)

            if i == NUM_Of_GENERATIONS - 1:
                num_of_overall_generations += gen_count
        best_string_lst.append((min_fitness, best_string))
    best_string_lst.sort(key=lambda x: x[0])
    best_string = best_string_lst[0][1]
    return best_string, num_of_overall_generations


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


if __name__ == '__main__':
    algo_type = input("Please choose the algorithm type R/D/L:")

    file_name = "enc.txt"

    if algo_type == "R":
        best, num_of_generations = run_regular_algo(file_name)
    elif algo_type == "D":
        best, num_of_generations = run_darwin_algo(file_name)
    elif algo_type == "L":
        best, num_of_generations = run_lamarck_algo(file_name)
    else:
        print("Invalid input")
        exit(1)
    # save the best string to a file named perm.txt
    abc_lst = list(ABC_SET)
    abc_lst.sort()
    with open("perm.txt", "w") as f:
        for letter in abc_lst:
            f.write(letter.lower() + " " + best[letter] + "\n")
    f.close()
    # save the plaintext to a file named plain.txt
    permute_file(best, file_name, "plain.txt")
    print("the overall number of generations is: " + str(num_of_generations))
    # ask the user to press enter to exit the program
    input("Press Enter to exit")
