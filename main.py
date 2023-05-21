import Fitness_class as fit
from generation_functions import *
from init_varibals import *


# use niching to find the best string
def start(file_name):
    fitness = fit.Fitness(file_name)
    diff_population_lst = []
    for i in range(10):
        diff_population_lst.append(init_first_generation(GENERATION_SIZE))
    for i in range(1, 1000):
        fitness_lst_lst = []
        best_fitness_lst = []
        for j in range(10):
            fitness_lst_lst.append([fitness.overall_fitness(string) for string in diff_population_lst[j]])
            best_fitness_lst.append(min(fitness_lst_lst[j]))
            diff_population_lst[j] = generate_next_generation(diff_population_lst[j], ABC_SET, fitness_lst_lst[j])
        if i % 100 == 0:
            # exchange genetic material between the populations
            # combine all the populations
            all_population_lst = []
            all_fitness_lst = []
            for population in diff_population_lst:
                all_population_lst += population
            for fitness_lst in fitness_lst_lst:
                all_fitness_lst += fitness_lst
            all_population_lst = generate_next_generation(all_population_lst, ABC_SET, all_fitness_lst)
            # split the combined population to 10 populations
            diff_population_lst = []
            for k in range(10):
                diff_population_lst.append(all_population_lst[k * GENERATION_SIZE:(k + 1) * GENERATION_SIZE])
        print("Generation: " + str(i) + " Best Fitness: " + str(min(best_fitness_lst)))


def run_genetic_algo(file_name):
    fitness = fit.Fitness(file_name)
    best_string_lst = []
    for j in range(10):
        curr_gen = generate_initial_guesses(GENERATION_SIZE, fitness)
        gen_count = 0
        best_string = ""
        best_fitness = float("inf")
        best_fitness_count = 0
        min_fitness = float("inf")
        for i in range(1000):
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
                break
            # check for convergence
            # convergence = check_convergence(curr_gen, fitness_lst)
            # if convergence:
            #     # mutate all the strings in the generation
            #     curr_gen = [mutate_permutation_dict(string, 0.2) for string in curr_gen]
            #     print("Convergence")
            curr_gen = generate_next_generation(curr_gen, ABC_SET, fitness_lst)
            print(str(j) + " Generation: " + str(gen_count) + " Best Fitness: " + str(
                min(fitness_lst)) + " Best String index:" + str(
                fitness_lst.index(min(fitness_lst))))
        best_string_lst.append((min_fitness, best_string))
    best_string_lst.sort(key=lambda x: x[0])
    best_string = best_string_lst[0][1]
    return best_string


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
    file_name = "enc.txt"
    # run the genetic algorithm
    best = run_genetic_algo(file_name)
    # save the best string to a file named perm.txt
    abc_lst = list(ABC_SET)
    abc_lst.sort()
    with open("perm.txt", "w") as f:
        for letter in abc_lst:
            f.write(letter.lower() + " " + best[letter] + "\n")
    f.close()
    # save the plaintext to a file named plain.txt
    permute_file(best, file_name, "plain.txt")

    print(best)
