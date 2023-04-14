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

def bulls_and_cows(guess, key): #count number of bulls and return as integer
    bull_num=0
    cow_num=len(set(guess).intersection(set(key)))
    for item1,item2 in zip(guess,key):
        if item1==item2:
            bull_num+=1
        else:
            pass
    cow_num-=bull_num
    return (bull_num,cow_num)

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
        bull_num,cow_num=bulls_and_cows(guess,key)
        print("The number of Bulls: ", bull_num)
        print("The number of Cows: ", cow_num)
        print('Your previous guesses (Guess, Bulls, Cows) were:')
        table.append((guess, bull_num, cow_num)) #add values to table
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
