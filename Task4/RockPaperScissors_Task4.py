#Task-4

#User Input: Prompt the user to choose rock, paper, or scissors.
#Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
#Game Logic: Determine the winner based on the user's choice and the computer's choice.
#Rock beats scissors, scissors beat paper, and paper beats rock.
#Display Result: Show the user's choice and the computer's choice.
#Display the result, whether the user wins, loses, or it's a tie.
#Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
#Play Again: Ask the user if they want to play another round.
#User Interface: Design a user-friendly interface with clear instructions and feedback.


import random
user_score = 0
computer_score = 0

def main():
    display_w()
    do_play = "y"
    while do_play == "y":
        do_play = play()

def display_w():
    print("WELCOME TO ROCK-PAPER-SCISSORS GAME")

def play():
    n=input("Enter your name:")
    u_choice=get_u_choice()
    c_choice=generate_c_choice()
    print("-------------------------------------------")
    print("Your Choice:",u_choice)
    print("Computer Choice: ",c_choice)
    print("-------------------------------------------")
    result = get_winner(u_choice,c_choice)
    global user_score, computer_score
    if(result=="Tie"):
        print("It's a TIE! The game must be played again to determine winner")
        return "y"
    else:
        print(result,"WON!")
        print("-------------------------------------------")
        if result == "USER":
           user_score += 1
        elif result == "COMPUTER":
           computer_score += 1
        print("User_Score=",user_score)
        print("Computer_Score=",computer_score)
        print("-------------------------------------------")
        return input("Play again (y/n)?")

def generate_c_choice():
    c=random.choice(["rock","paper","scissors"])
    return c

def get_u_choice():
    display_instructions()
    u=input("Enter your choice(rock/paper/scissors):")
    while not is_valid(u):
        print("Invalid Choice. Please Try Again")
        display_instructions()
        u=input("Enter your choice(rock/paper/scissors):")
    return u   

def display_instructions():
    print("-------------------------------------------")
    print("Type only one among following:")
    print("rock")
    print("paper")
    print("scissors")
    print("-------------------------------------------")

def is_valid(choice):
    if(choice=="rock" or choice=="paper" or choice=="scissors"):
        return True
    else:
        return False

def get_winner(a,b):
    if((a=="rock" and b=="scissors") or (a=="paper" and b=="rock") or (a=="scissors" and b=="paper")):
        return "USER"
    elif(a==b):
        return "TIE"
    else:
        return "COMPUTER"
    
main()


    

