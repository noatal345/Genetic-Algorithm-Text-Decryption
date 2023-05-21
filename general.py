from init_varibals import ABC_SET

def create_english_dictionary(filename):
    # create a hash set
    english_dict = set()
    # open filename and append each value in each row to the english dictionary.
    with open(filename) as f:
        for line in f:
            english_dict.add(line.upper().strip())
    # close file
    f.close()
    return english_dict


def create_dictionary(filename):
    new_dict = {}
    # open the filename and read each line.
    with open(filename) as f:
        for line in f:
            if line == "\t\n" or line == "\n" or line == "\t":
                break
            # if the line is empty or the line doesn't contain a "\t" char continue to the next line.
            if "\t" not in line:
                continue
            # split the line to key and value according to "\t" tab space.
            value, key = line.split("\t")
            # remove the "\n" from the key.
            key = key.strip()
            # convert the value to float.
            value = float(value)
            # add the key and value to the dictionary.
            new_dict[key] = value
    f.close()
    return new_dict


def count_words(file):
    num_of_words = 0
    with open(file, 'r') as f:
        for line in f:
            words = line.strip().split()
            num_of_words += len(words)
    f.close()
    return num_of_words


def file_letter_freq(file):
    file_letter_frequency = {}
    available_letters = ABC_SET.copy()
    # open the file
    with open(file, 'r') as f:
        # read the file
        file = f.read().upper()
        # count the number of time each letter appears in the file
        for letter in file:
            if letter.isalpha():  # Only count letters
                if letter in file_letter_frequency:
                    file_letter_frequency[letter] += 1
                else:
                    file_letter_frequency[letter] = 1
                    # remove the letter from the available_letters
                    available_letters.remove(letter)
    f.close()
    # add the letters that are not in the file to the file_letter_frequency dictionary
    for letter in available_letters:
        file_letter_frequency[letter] = 0
    # normalize the counts to get frequencies
    total_count = sum(file_letter_frequency.values())
    file_letter_frequency = {letter: count / total_count for letter, count in file_letter_frequency.items()}
    return file_letter_frequency


def file_two_letters_freq(file):
    file_2letter_frequency = {}
    # open the file
    with open(file, 'r') as f:
        # read the file
        file = f.read().upper()
        # count the number of time each letter appears in the file
        for i in range(len(file) - 1):
            two_letter = file[i:i + 2]
            if two_letter.isalpha():
                if two_letter in file_2letter_frequency:
                    file_2letter_frequency[two_letter] += 1
                else:
                    file_2letter_frequency[two_letter] = 1
        # normalize the counts to get frequencies
        total_count = sum(file_2letter_frequency.values())
        file_2letter_frequency = {two_letter: count / total_count for two_letter, count in
                                  file_2letter_frequency.items()}
    f.close()
    return file_2letter_frequency
