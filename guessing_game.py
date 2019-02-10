"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

print("""
====================================
Welcome to the Number Guessing Game!
====================================
    
    """)


attempts = 1
high_score = 0 

while True:
    random_number = random.randint(1,10)

    while True:

        
        try:
            guess = int(input("\n\nPick a number between 1 and 10  "))
            if (guess > 0 and guess < 11):
                if guess > random_number:
                    print("\n>>>>>It's lower<<<<<")
                    attempts += 1
                    continue
                elif guess < random_number:
                    print("\n>>>>>It's higher<<<<<")
                    attempts += 1
                    continue
                else:
                    guess = random_number
                    if attempts == 1:
                        print("\nWow, you guessed the number on your first try!")
                    else:
                        print("\nYou win! You guessed {}, the correct number. It took you {} tries.".format(guess, attempts))
                    
                    
                    if high_score == 0:
                        high_score = attempts
                        print("\nCongratulations, you have the new high score!")
                    elif attempts < high_score:
                        high_score = attempts
                        print("\nCongratulations, you have the new high score!")
                    else:
                        print("The current high score is: {}".format(high_score))
                    
                    attempts = 1 
                    break
            else:
                print("You many only pick a number between 1 and 10.")
        except ValueError:
            print("Oops, that is not a valid number. Please use a digit such as '9' only.")

    while True:
        play_again = input("\n\nDo you want to play again?  (y/n) ")
        if play_again.lower() == 'y':
            print("""
=====================================
Great! The high score to match or beat is {}.
=====================================
                """.format(high_score))
            break
        elif play_again.lower() == 'n':
            print("""
=====================================
   Thanks for playing. Game Over.
=====================================
""")
            exit()
        else:
            print("\nThat is not a valid entry.")
    continue

        



    



if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
