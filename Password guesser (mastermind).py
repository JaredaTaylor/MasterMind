from random import randint

def passw():
    password = []
    number = randint(0, 9)
    password.append(number)
    while len(password) != 4:
        number = randint(0, 9)
        if number not in password:
            password.append(number)
    return password

def guess():
    guess = []
    print("Insert guess")
    guess = list(input(": "))
    guess = list(map(int, guess))
    while len(guess) != 4:
        print("Wrong number of digits")
        guess = list(input(": "))
        guess = list(map(int, guess))
    return guess
    

def compare():
    tries = 0
    password = passw()
    places = [0,1,2,3]
    print("------------------------------WELCOME------------------------------")
    print("|This is mastermind, a four digit password is randomly generated. |")
    print("|Please guess the password with 5 guesses, goodluck!              |")
    print("|  ✓ means that you guessed the correct number and position      |")
    print("|  O means that you guessed the correct number but wrong position |")
    print("|  X means that you guessed the wrong number and wrong position   |")
    print("-------------------------------------------------------------------")
    gues = guess()
    pos = [0,1,2,3]
    while tries != 4:
        if password == gues:
            pos = ["✓","✓","✓","✓"]
            print("Congratualtions! You solved the password!")
            break
        for i in places:
            #print(gues[i])
            #print(password[i])
            #print("-----------------------")
            if gues[i] == password[i]:
                pos[i] = "✓"
            elif gues[i] in password and gues[i] != password[i]:
                pos[i] = "O"
            else:
                pos[i] = "X"
        print(pos)
        gues = guess()
        
        tries += 1
    if password != gues:
            print("Better luck next time! You didn't guess the correct code.")
            print("the code was", password)


compare()
