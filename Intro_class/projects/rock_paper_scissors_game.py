from random import choice

print("Rule of the game".center(60, "="))
print("""
        Rock smashes scissors.
        Paper covers rock.
        Scissors cut paper.
        """)
computer_sco=0
player_sco=0
tie=0
count=0
while True:
    poss_ac=["rock", "paper", "scissors"]
    user_guess=input("please enter one of these'rock' or 'paper' or 'scissors': ")
    user_guess=user_guess.lower()
    comp_guess=choice(poss_ac)
    print(f"your choice is {user_guess} computer choice is {comp_guess}")
    if user_guess==comp_guess:
        print(f"It is tie, Both select {user_guess}")
        tie +=1
    elif user_guess=='rock':
        if comp_guess=='paper':
            print("Oops, You lose Computer won!")
            computer_sco +=1
            print(f"computer Won:{computer_sco}")
        else:
            print("Congradulations, You won!")
            player_sco +=1 
            print(f"You Won: {player_sco}")
    elif user_guess=='scissors':
        if comp_guess=='rock':
            print("Oops, You lose Computer won")
            computer_sco +=1
            print(f"computer Won:{computer_sco}")
        else:
            print("Congrats, You won!")
            player_sco +=1 
            print(f"You Won: {player_sco}")
    elif user_guess=='paper':
        if comp_guess=='scissors':
            print("Oops, You lose Computer won")
            computer_sco +=1
            print(f"computer Won:{computer_sco}")
        else:
            print("Congrats, You won!")
            player_sco +=1 
            print(f"You Won: {player_sco}")
    else:
        print("please enter correct value:")
    play_again=input("Do you want to play again y/n: ")
    play_again=play_again.upper()
    if play_again != 'Y':
        break
    
total_count= tie + computer_sco + player_sco
print("Game Statstics".center(100,'+'))
print (f"Total prompt: {total_count}")
print(f"Tie: {tie}")
print (f"Computer won: {computer_sco}")
print(f"You Won: {player_sco}")