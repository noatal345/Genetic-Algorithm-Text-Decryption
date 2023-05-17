from fitness import *

# define parameters:
encoded_file = "enc.txt"
common_words_set = create_english_set("dict.txt")

# save the number of words and chars from the encoded file into parameters
num_of_words, num_of_chars = count_words("enc.txt")
# save the characters frequencies in dictionaries
english_2letter_frequency = create_dictionary("Letter2_Freq.txt")
english_letter_frequency = create_dictionary("Letter_Freq.txt")


d = {'A': 'Y', 'B': 'X', 'C': 'I', 'D': 'N', 'E': 'T', 'F': 'O', 'G': 'Z', 'H': 'J', 'I': 'C', 'J': 'E', 'K':
    'B', 'L': 'L', 'M': 'D', 'N': 'U', 'O': 'K', 'P': 'M', 'Q': 'S', 'R': 'V', 'S': 'P', 'T': 'Q', 'U': 'R', 'V':
    'H', 'W': 'W', 'X': 'G', 'Y': 'A', 'Z': 'F'}


fitness = overall_fitness(d, "enc.txt", num_of_words, common_words_set, english_letter_frequency,
                                      english_2letter_frequency)
print(fitness)
