import random

while True:
     choice = input("will u play the game (y/n):").lower()
     
     
     if choice == "n":
        print("thanks for playing") 
        break 
    
     if choice == "y":
        computer = random.choice(["rock", "p" , "s"])
     player = input("Choose (rock/p/s): ").lower()

     if player not in ["rock", "p", "s"]:
            print("Invalid input")
            continue
     if computer == player:
        print("this was a tie")

     elif (
    (player == "rock" and computer == "s") or
    (player == "p" and computer == "rock") or
    (player == "s" and computer == "p")
):
      print("You win!")
     else:
        print("you loose")
        print("computer chose:" , computer)
    
else: 
      print("invalid choice")
