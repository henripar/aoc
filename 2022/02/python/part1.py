with open("../input.txt") as file:
    plays = file.read()
file.close()

plays_list = plays.split("\n")
plays_list.pop()

my_points = 0

for play in plays_list:
    opponent_pick = play.split(' ')[0]
    my_pick = play.split(' ')[1]

    # Opponent picks rock
    if opponent_pick == 'A' and my_pick == 'Z':
        print('opponent picks rock and you pick scissors, you lost.')
        my_points = my_points + 3 + 0;
    if opponent_pick == 'A' and my_pick == 'X':
        print('opponent picks rock and you pick rock, its a draw.')
        my_points = my_points + 1 + 3;
    if opponent_pick == 'A' and my_pick == 'Y':
        print('opponent picks rock and you pick paper, you win.')
        my_points = my_points + 2 + 6;

    # Opponent picks paper

    if opponent_pick == 'B' and my_pick == 'Z':
        print('opponent picks paper and you pick scissors, you win.')
        my_points = my_points + 3 + 6;
    if opponent_pick == 'B' and my_pick == 'X':
        print('opponent picks paper and you pick rock, you lost.')
        my_points = my_points + 1 + 0;
    if opponent_pick == 'B' and my_pick == 'Y':
        print('opponent picks paper and you pick paper, its a draw.')
        my_points = my_points + 2 + 3;

    # Opponent picks scissors

    if opponent_pick == 'C' and my_pick == 'Z':
        print('opponent picks scissors and you pick scissors, its a draw.')
        my_points = my_points + 3 + 3;
    if opponent_pick == 'C' and my_pick == 'X':
        print('opponent picks scissors and you pick rock, you win.')
        my_points = my_points + 1 + 6;
    if opponent_pick == 'C' and my_pick == 'Y':
        print('opponent picks scissor and you pick paper, you lose.')
        my_points = my_points + 2 + 0;

print(my_points)