with open("../input.txt") as file:
    input = file.read()
file.close()

expense_report = input.split("\n")
expense_report.pop()

expense_report = [int(expense) for expense in expense_report]

expense_report.sort()

def part2(expense_report):
    for base_index, base in enumerate(expense_report):
        rem = 2020 - base
        left_index = base_index + 1
        right_index = len(expense_report) - 1
        while (left_index < right_index):
            if expense_report[left_index] + expense_report[right_index] == rem:
                return base * expense_report[left_index] * expense_report[right_index]
            if expense_report[left_index] + expense_report[right_index] > rem:
                right_index -= 1
            else:
                left_index += 1

print(part2(expense_report))