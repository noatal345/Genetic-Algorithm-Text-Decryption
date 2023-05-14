

def create_english_dictionary(filename):
    # create a hash set
    english_dict = set()
    # open filename and append each value in each row to the english dictionary.
    with open(filename) as f:
        for line in f:
            english_dict.add(line.strip())
    #close file
    f.close()
    return english_dict


# This function receives a path to a txt file as argument.
# The function reads the file and creates a dictionary from the file.
# The function returns the new dictionary where the key is the first word and the value is the second of each row.
def create_dictionary(filename):
    new_dict = {}
    # open the filename and read each line.
    with open(filename) as f:
        for line in f:
            # if the line is empty or the line doesn't contain a "\t" char continue to the next line.
            if "\t" not in line:
                continue
            # split the line to key and value according to "\t" tab space.
            value, key = line.split("\t")
            # remove the "\n" from the key.
            key = key.strip()
            # add the key and value to the dictionary.
            new_dict[key] = value
    f.close()
    return new_dict


def count_words(filename):
    characters = set()
    characters.add(".")
    characters.add(",")
    characters.add(" ")
    characters.add("\n")
    characters.add(";")
    new_word_delimiter = set()
    new_word_delimiter.add(" ")
    new_word_delimiter.add("\n")
    numer_of_words = 0
    number_of_char = 0
    special_char = 0
    flag_word = False
    total_chars = 0
    # open filename and count the number characters and the number of words in the file.
    with open(filename) as f:
        for line in f:
            for char in line:
                total_chars += 1
                if char in characters:
                    special_char += 1
                    if char in new_word_delimiter:
                        if flag_word:
                            numer_of_words += 1
                            flag_word = False
                else:
                    flag_word = True
    number_of_char = total_chars - special_char
    print("total =", total_chars)
    print("special =", special_char)
    #close file
    f.close()
    return numer_of_words, number_of_char




# the main program
# create a dictionary of english words according to the dictionary file.
english_dict = create_dictionary("dict.txt")
num_of_words, num_of_chars = count_words("enc.txt")
print("number of chars = ", num_of_chars)
print("number of words = ", num_of_words)
a = create_dictionary("Letter2_Freq.txt")
print(a.items())
print(a.keys())
print(a.values())
b = create_dictionary("Letter_Freq.txt")
print(b.items())
print(b.keys())
print(b.values())

print("hadar")