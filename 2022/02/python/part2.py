with open("../input.txt") as file:
    plays = file.read()
file.close()

plays_list = plays.split("\n")
plays_list.pop()

my_points = 0

for play in plays_list:
    opponent_pick = play.split(' ')[0]
    my_plan = play.split(' ')[1]

    if my_plan == 'X':
        print('Plan is to lose.')
        match opponent_pick:
            case 'A':
                print('opponent picks rock and plan is to lose. So, you pick scissors.')
                my_points = my_points + 3 + 0;
            case 'B':
                print('opponent picks paper and plan is to lose. So, you pick rock.')
                my_points = my_points + 1 + 0;
            case 'C':
                print('opponent picks scisors and plan is to lose. So, you pick paper.')
                my_points = my_points + 2 + 0;

    if my_plan == 'Y':
        print('Plan is to draw.')
        match opponent_pick:
            case 'A':
                print('opponent picks rock and plan is to draw. So, you pick rock.')
                my_points = my_points + 1 + 3;
            case 'B':
                print('opponent picks paper and plan is to draw. So, you pick paper.')
                my_points = my_points + 2 + 3;
            case 'C':
                print('opponent picks scissors and plan is to draw. So, you pick scissors.')
                my_points = my_points + 3 + 3;

    if my_plan == 'Z':
        print('Plan is to win.')
        match opponent_pick:
            case 'A':
                print('opponent picks rock and plan is to win. So, you pick paper.')
                my_points = my_points + 2 + 6;
            case 'B':
                print('opponent picks paper and plan is to win. So, you pick scissors.')
                my_points = my_points + 3 + 6;
            case 'C':
                print('opponent picks scissors and plan is to win. So, you pick rock.')
                my_points = my_points + 1 + 6;

print(my_points)