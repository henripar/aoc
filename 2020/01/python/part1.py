with open("../input.txt") as file:
    input = file.read()
file.close()

expense_report = input.split("\n")
expense_report.pop()

expense_report = [int(expense) for expense in expense_report]

print(expense_report)

for expense in expense_report:
    for expense2 in expense_report:
        if expense + expense2 == 2020:
            print(expense * expense2)
