import random
def receive_input():
    x = str()
    c=False
    while c==False:
        x = str(input("Enter 4 digit number: "))
        c=True
        if len(x)!=4:
            c=False
        elif x.isdigit()==False:
            c=False
        else:
            pass
        for i in x:
            if x.count(i)!=1:
                c=False
                break
            else:
                pass
        if c==False:
            print("Enter valid number")
        else:
            pass
    return x
def random_key():
    c=False
    while c==False:
        x=random.randint(122,9877)
        c=True
        if len(str(x))!=4:
            c=False
        else:
            pass
        for i in str(x):
            if str(x).count(i)!=1:
                c=False
                break
            else:
                pass
    if len(str(x))==3:
           x='0'+str(x)
    else:
        x=str(x)
    return x
def position(guess, key):
    n=0
    for i in range(4):
        if guess[i]==key[i]:
            n+=1
        else:
            pass
    return str(n)
def exist(guess, key):
    n=0
    for i in range(4):
        if guess[i] in key:
            n+=1
        else:
            pass
    n=n-int(position(guess, key))
    return str(n)
def game():
    key=random_key()
    table=list()
    for i in range(12):
        x=receive_input()
        if x==key:
            print('You guessed right :)')
            print('The key is', key)
            print("It took you", i+1, 'guesses')
            break
        else:
            pass
        print("The number of Bulls: ", position(x,key))
        print("The number of Cows: ", exist(x,key))
        print('Your previous guesses (Guess, Bulls, Cows) were:')
        table.append((x,position(x,key),exist(x,key)))
        for line in table:
            print(line[0],line[1],line[2])
    if x!=key:
        print("You lose :(")
        print("The key is", key)
        print("Try better next time.")
    print("Thank you for playing")
def game_loop():
    while True:
        game()
        print("Play another game? Press y for Yes, and n for No.")
        x=input().strip()
        while x not in 'yn':
            print("Please enter either y or n")
            x=input().strip()
        if x=='y':
            continue
        else:
           break 
game_loop()
