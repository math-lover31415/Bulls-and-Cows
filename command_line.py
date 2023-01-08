from random import sample #module for generating key

def receive_input():
    while True: #loop that will keep asking for input until it is valid.
        inp = str(input("Enter 4 digit number: "))
        if len(inp)!=4: #imput must be 4 characters long
            print("Please enter a valid number")
            continue
        elif not inp.isdigit(): #input must be a number
            print("Please enter a valid number")
            continue
        else:
            pass
        try:
            for i in inp: #To see that no digit is repeated
                assert inp.count(i)==1
        except AssertionError:
            print("Please enter a valid number")
            continue
        break
    return inp

def random_key(): #generates a random key as string
    rand_list=sample(range(10),4) #use random mosule to get 4 random non repeating single digit int values
    key=str()
    for num in rand_list: #make a 4 digit numbers with string addition of the 4 one digit numbers
        key+=str(num)
    return key

def bulls(guess, key): #count number of bulls and return as integer
    count=0
    for item1,item2 in zip(guess,key):#compare elements in guess and keys at the same index
        if item1==item2:
            count+=1
        else:
            pass
    return count

def cows(guess, key):
    count=0
    for index in range(4): #loop to count how many numbers are common in guess and keys
        if guess[index] in key:
            count+=1
        else:
            pass
    #count=bulls+cows
    cow=count-bulls(guess, key)
    return cow

def game(): #The main code for the game
    key=random_key() #generate a random key
    table=list() #create a list to store our previous guesses
    for n in range(1,13): #the players get 12 turns
        guess=receive_input()
        if guess==key:
            print('You guessed right :)')
            print('The key is', key)
            print("It took you", n, 'guesses')
            break
        else:
            pass
        print("The number of Bulls: ", bulls(guess,key))
        print("The number of Cows: ", cows(guess,key))
        print('Your previous guesses (Guess, Bulls, Cows) were:')
        table.append((guess, bulls(guess,key) , cows(guess,key))) #add values to table
        for line in table:
            print(line[0],line[1],line[2], sep=', ')
    if guess!=key:
        print("You lose :(")
        print("The key is", key)
        print("Try better next time.")
    print("Thank you for playing")

def game_loop(): #A loop that will allow the players to play multiple times.
    while True:
        game()
        print("Play another game? Press y for Yes, and n for No.")
        x=input().strip()
        while x not in 'yn': #to enure the input is either 'y' or 'n'
            print("Please enter either y or n")
            x=input().strip()
        if x=='y':
            continue
        else:
           break 

game_loop()
