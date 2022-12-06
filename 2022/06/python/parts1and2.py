with open("../input.txt") as file:
    input = file.read()
file.close()

def get_last_characters(amount, characters):
    characters = characters[len(characters) - amount : len(characters)]
    last_chars = []
    for character in characters:
        last_chars.append(character)
    return last_chars

def find_unique_values_in_list(values_list):
    unique_list = []
    for x in values_list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def find_start_points(marker_length, input):
    letters = []
    counter = 0
    for letter in input:
        counter += 1
        letters.append(letter)
        last_characters = get_last_characters(marker_length, letters)
        unique_characters_in_last_characters = find_unique_values_in_list(last_characters)
        if len(unique_characters_in_last_characters) == marker_length and [x != None for x in unique_characters_in_last_characters]:
            print(counter)
            return

find_start_points(4, input)
find_start_points(14, input)
