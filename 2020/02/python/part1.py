with open("../input.txt") as file:
    input = file.read()
file.close()

passwords_list = input.split("\n")
passwords_list.pop()

passwords_list = [pw.split(" ") for pw in passwords_list]

good_pw_count = 0;

for password in passwords_list:
    pw_length = len(password[2])
    pw = password[2]
    pw_count = pw.count(password[1][0])

    if pw_count  >= int(password[0].split('-')[0]) and pw_count <= int(password[0].split('-')[1]):
        good_pw_count += 1

print(good_pw_count)
