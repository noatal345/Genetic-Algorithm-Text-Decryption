import general


class Fitness:
    def __init__(self, file):
        self.num_of_words_in_file = general.count_words(file)
        self.common_words_set = general.create_english_dictionary("dict.txt")
        self.english_letter_frequency = general.create_dictionary("Letter_Freq.txt")
        self.english_2letter_frequency = general.create_dictionary("Letter2_Freq.txt")
        self.file_letter_frequency = general.file_letter_freq(file)
        self.file_2letter_frequency = general.file_two_letters_freq(file)
        self.original_file = file

    def __common_words_fitness(self, optional_alphabet_dictionary):
        fittness = 0
        with open(self.original_file, 'r') as f:
            for line in f:
                # Split each line into words
                words = line.upper().strip().split()
                # for each word in the line, use the optional_alphabet_dictionary to decrypt the word
                # and check if the decrypted word appears in the set of common words
                for word in words:
                    decrypted_word = ""
                    for letter in word:
                        if letter.isalpha():
                            decrypted_word += optional_alphabet_dictionary[letter]
                        else:
                            decrypted_word += letter
                    if decrypted_word in self.common_words_set:
                        fittness += 1
        f.close()
        return (self.num_of_words_in_file - fittness) / self.num_of_words_in_file

    def __letter_frequency_fitness(self, optional_alphabet_dictionary, flag):
        if flag == 1:
            org_file_letter_frequency = self.file_letter_frequency
            english_frequency = self.english_letter_frequency
        if flag == 2:
            org_file_letter_frequency = self.file_2letter_frequency
            english_frequency = self.english_2letter_frequency
        fitness = 0
        optional_alphabet_letter_frequency = {}
        # join the optional_alphabet_dictionary and org_file_letter_frequency by the key
        for key in optional_alphabet_dictionary:
            if key in org_file_letter_frequency:
                optional_alphabet_letter_frequency[optional_alphabet_dictionary[key]] = org_file_letter_frequency[key]
            else:
                optional_alphabet_letter_frequency[optional_alphabet_dictionary[key]] = 0
        # calculate the fitness
        for letter in optional_alphabet_letter_frequency:
            if letter in english_frequency:
                fitness += pow(optional_alphabet_letter_frequency[letter] - english_frequency[letter], 2)
        return fitness / len(english_frequency)

    def overall_fitness(self, optional_alphabet_dictionary):
        w1, w2, w3 = 0.5, 0.25, 0.25
        fitness = w1 * self.__common_words_fitness(optional_alphabet_dictionary) + w2 * self.__letter_frequency_fitness(
            optional_alphabet_dictionary,1) + w3 * self.__letter_frequency_fitness(optional_alphabet_dictionary,2)

        return fitness
