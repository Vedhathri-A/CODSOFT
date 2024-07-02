Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... def get_player_choice():
...     while True:
...         choice = input("Choose rock, paper, or scissors: ").lower()
...         if choice in ["rock", "paper", "scissors"]:
...             return choice
...         print("Invalid choice. Please try again.")
... 
... def get_computer_choice():
...     return random.choice(["rock", "paper", "scissors"])
... 
... def determine_winner(player_choice, computer_choice):
...     if player_choice == computer_choice:
...         return "It's a tie!"
...     elif (
...         (player_choice == "rock" and computer_choice == "scissors") or
...         (player_choice == "paper" and computer_choice == "rock") or
...         (player_choice == "scissors" and computer_choice == "paper")
...     ):
...         return "You win!"
...     else:
...         return "Computer wins!"
... 
... def play_game():
...     player_choice = get_player_choice()
...     computer_choice = get_computer_choice()
...     print(f"You chose {player_choice}. The computer chose {computer_choice}.")
...     print(determine_winner(player_choice, computer_choice))
... 
