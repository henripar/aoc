with open("../input.txt") as file:
    calories_per_elf = file.read()
file.close()

calories_per_elf = calories_per_elf.split("\n\n")
calories_per_elf_combined = []

for i, value in enumerate(calories_per_elf):
    current_elfs_calories_list = calories_per_elf[i].split("\n")
    current_elfs_calories_combined = 0
    
    print(current_elfs_calories_list)
    
    for calories in current_elfs_calories_list:
        if calories != '':
            current_elfs_calories_combined += int(calories)
        
    calories_per_elf_combined.append(current_elfs_calories_combined)
    
calories_per_elf_combined.sort(reverse=True)

print(calories_per_elf_combined[0])

print(calories_per_elf_combined[0] + calories_per_elf_combined[1] + calories_per_elf_combined[2])