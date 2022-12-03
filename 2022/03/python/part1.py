import string

with open("../input.txt") as file:
    backpack_items = file.read()
file.close()

backpack_items_list = backpack_items.split("\n")

# helpers

def split_string_in_half(str):
    string1 = slice(0, len(str)//2)
    string2 = slice(len(str)//2, len(str))
    return [str[string1], str[string2]]

def find_common_characters(s1, s2):
    for index, i in enumerate(s1):
        common_char =  i if (i in s2) else False
        if common_char != False or '':
            return common_char

def count_points(letter):
    alphabet_uppercase = list(string.ascii_uppercase)
    alphabet_lowercase = list(string.ascii_lowercase)

    if letter in alphabet_uppercase:
        points = alphabet_uppercase.index(letter) + 27
        return points

    if letter in alphabet_lowercase:
        points = alphabet_lowercase.index(letter) + 1
        return points

def calculate_priorities_sum(items_list):
    total_points = 0

    for backpack in items_list:
        [first_compartment, second_compartment] = split_string_in_half(backpack)

        common_chars = find_common_characters(first_compartment, second_compartment)

        points = count_points(common_chars)

        if points is not None:
            total_points = total_points + points
    print(total_points)


calculate_priorities_sum(backpack_items_list)