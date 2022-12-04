with open("../input.txt") as file:
    input = file.read()
file.close()

assignment_pairs = input.split("\n")

assignment_pairs = [x.split(',') for x in assignment_pairs]

partial_matches_amount = 0

for assignment_pair in assignment_pairs:
    first_assignment_start = int(assignment_pair[0].split('-')[0])
    first_assignment_end = int(assignment_pair[0].split('-')[1])
    second_assignment_start = int(assignment_pair[1].split('-')[0])
    second_assignment_end = int(assignment_pair[1].split('-')[1])

    if first_assignment_start >= second_assignment_start and first_assignment_start <= second_assignment_end:
        partial_matches_amount += 1

    elif second_assignment_start >= first_assignment_start and second_assignment_start <= first_assignment_end:
        partial_matches_amount += 1

print(partial_matches_amount)
