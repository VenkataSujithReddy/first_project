import random


secret = random.randint(1 , 100)

while True: 
    guess = int(input("guess the number:"))

    if guess == secret:
        print("you gussed correct")
        break
    elif guess < secret:
        print("higher")
    
else:     
    guess > secret 
    print("lower")
