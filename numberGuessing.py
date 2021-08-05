import random
number = random.randint(1, 10)

numberOfGuess=0

while numberOfGuess <5:
    guess=int(input("Guess a number: "))
    numberOfGuess=numberOfGuess+1
    if(guess < number):
         print('Your guess is too low')
    
    elif(guess > number):
         print('Your guess is too high')
    
    elif(guess == number):
         print('Your guess is Correct')
         break
    elif(numberOfGuess==5):
        print("The correct number is" ,number)
        print("Better luck next time")
    

    
    