# import de la function random
import random

# intialisation des variables pour le nombre de victoires joueurs et le nombre de victoires ordinateur.
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

# On crée une boucle infinie (et oui)
while True:
    # on demande à l'utilisateur de produire une entrée en réponse à la question, et on la récupère
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        # on gère la condition de sortie de la boucle
        break

    # on ignore une réponse de l'utilisateur ne correspondant à rien
    if user_input not in options:
        continue
    # on parmaètre le tour de l'ordinateur avec des coups aléatoires dans les valeurs possibles
    random_number = random.randint(0, 2)
    #rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked ", computer_pick + ".")

    # on gère les conditions de victoires de l'utilisateur
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

# en cas de sortie (si l'utilisateur répond "q")
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("GoodBye!")