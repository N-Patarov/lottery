from random import randint

correct_combination=[]

for i in range(6):
    num = randint(6,49)
    if num not in correct_combination:
        correct_combination.append(num)
    else:
        if num not in correct_combination:
            correct_combination.append(randint(6,49))


full_guess=[]
correct_guesses=[]

score=0

while len(full_guess) < 6:
    try:
        guess=int(input("type 6 number from 6-49: "))
        while (guess not in full_guess) & ((guess >= 6) and (guess <= 49)):
            full_guess.append(guess)
        else:
            if guess not in full_guess: print("you can choose a number only once")
            if (guess <= 6) or (guess >= 49):print("You can only choose numbers between 6 & 49!")



    except ValueError:
        print("You can only choose numbers between 6 & 49!")

for i in range(len(full_guess)):
    n=full_guess[i]
    m=correct_combination[i]
    if n in correct_combination: score+=1



print("your guess is")
print(full_guess)
print("the correct combination is")
print(correct_combination)
print("your score is")
print(score)