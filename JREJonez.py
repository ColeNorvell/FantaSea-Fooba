# J.R.E. Jonze Pro Football
#
# Developed by students and their instructor
# at theCoderSchool in Flower Mound, TX
#
# Contributors:
# Cole N. (Student)
# Tanner A. (Student)
# Chris P. (Instructor)

# Greet User
import time
import random
print("Welcome to J.R.E. Jonze Pro Football")
time.sleep(1)
print("You are J.R.E. Jonze, the billionaire oil tycoon and the owner of the world's most valuable team in sports.")
time.sleep(1.5)
print("As owner, general manager, and coach, you will call the plays for Dallas.")
time.sleep(2)

opponent = random.randint(1, 31)

if opponent == 1:
    opponent = "Arizona"
elif opponent == 2:
    opponent = "Atlanta"
elif opponent == 3:
    opponent = "Baltimore"
elif opponent == 4:
    opponent = "Buffalo"
elif opponent == 5:
    opponent = "Carolina"
elif opponent == 6:
    opponent = "Chicago"
elif opponent == 7:
    opponent = "Cincinnati"
elif opponent == 8:
    opponent = "Cleveland"
elif opponent == 9:
    opponent = "Denver"
elif opponent == 10:
    opponent = "Detroit"
elif opponent == 11:
    opponent = "Green Bay"
elif opponent == 12:
    opponent = "Houston"
elif opponent == 13:
    opponent = "Indianapolis"
elif opponent == 14:
    opponent = "Jacksonville"
elif opponent == 15:
    opponent = "Kansas City"
elif opponent == 16:
    opponent = "Los Angeles"
elif opponent == 17:
    opponent = "Los Angeles"
elif opponent == 18:
    opponent = "Miami"
elif opponent == 19:
    opponent = "Minnesota"
elif opponent == 20:
    opponent = "New England"
elif opponent == 21:
    opponent = "New Orleans"
elif opponent == 22:
    opponent = "New York"
elif opponent == 23:
    opponent = "New York"
elif opponent == 24:
    opponent = "Oakland"
elif opponent == 25:
    opponent = "Philadelphia"
elif opponent == 26:
    opponent = "Pittsburg"
elif opponent == 27:
    opponent = "San Francisco"
elif opponent == 28:
    opponent = "Seattle"
elif opponent == 29:
    opponent = "Tampa Bay"
elif opponent == 30:
    opponent = "Tennessee"
elif opponent == 31:
    opponent = "Washington"


print("Your opponent this week will be " + opponent + ".")

# Initialize Game Variables
player_score = 0
opponent_score = 0
down = 1
yards_needed_for_first_down = 0
team_with_possesion = "Dallas"
yard_line = 0 # yardLine -50 to 50
print("Heads or tails? h for heads t for tails.")
coin_guess = input(">")
coin_flip = random.randint, (0,1)
if coin_flip == 0:
    coin = "h"
else:
    coin = "t"

if coin_guess == coin:
    print("You win the toss; your team goes first.")
    #Dallas goes first
else:
    print("You lose the toss; the other team goes first.")
    #Other team goes first

# Main Game Loop
'''
game_over = False
while game_over == False:
    # do stuff
'''
