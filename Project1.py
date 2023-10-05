import random

def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value,max_value)
    return roll


while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <= 4:
            break
        else: 
            print("Enter valid number of players(2-4)")
    else:
        print("Invalid, try again")

max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    for player_idx in range(players):
        print("\n It's Player Number ",player_idx + 1,"'s turn!")
        print("Your current score is ", players_scores[player_idx],"\n")
        current_score = 0

        while True:
            should_roll = input("would you like to roll (y)?")
            if should_roll.lower()!= "y":
                break
            value = roll()
            if value == 1:
                print("Oops! You rolled 1! Turn Done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:",value)

            print("Your current score is:",current_score)

        players_scores[player_idx] += current_score
        print("Your score is :" , players_scores[player_idx])

max_score = max(players_scores)

winning_idx = players_scores.index(max_score)
print("\n Player Number ", winning_idx + 1 , " is the winner with a total score of:" , max_score)
         
        