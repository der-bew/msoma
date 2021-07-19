from random import choice

print("Rule of the game".center(60, "="))

while True:
    poss_ac=["rock", "paper", "scissors"]
    user_guess=input("please enter one of these'rock' or 'paper' or 'scissors': ")
    user_guess=user_guess.lower()
    comp_guess=choice(poss_ac)
    print(f"your choice is {user_guess} computer choice is {comp_guess}")
    if user_guess==comp_guess:
        print(f"It is tie, Both select {user_guess}")
    elif user_guess=='rock':
        if comp_guess=='paper':
            print("Oops, You lose Computer won!")
        else:
            print("Congradulations, You won!")
    elif user_guess=='scissors':
        if comp_guess=='rock':
            print("Oops, You lose Computer won")
        else:
            print("Congrats, You won!")
    elif user_guess=='paper':
        if comp_guess=='scissors':
            print("Oops, You lose Computer won")
        else:
            print("Congrats, You won!") 
    else:
        print("please enter correct value:")
    play_again=input("Do you want to play again y/n: ")
    play_again=play_again.upper()
    if play_again != 'Y':
        break
