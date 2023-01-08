import tkinter as tk
from random import sample

def random_key(): #generates a random key as string
    rand_list=sample(range(10),4) #use random mosule to get 4 random non repeating single digit int values
    key=str()
    for num in rand_list: #make a 4 digit numbers with string addition of the 4 one digit numbers
        key+=str(num)
    return key

rand=random_key()
correct_guess_flag=False

def check_number(inp):
    inp=str(inp)
    if len(inp)!=4:
        return False
    elif not inp.isdigit(): #input must be a number
        return False
    else:
        pass
    for i in inp: #To see that no digit is repeated
        if inp.count(i)!=1:
            return False
    return True

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
    
def f():
    global n, correct_guess_flag
    if correct_guess_flag:
        return None
    number=entry.get().strip()
    if n<12:
        if check_number(number):
            values=(number, bulls(number,rand), cows(number,rand))
            n+=1
            for i in range(3):
                tk.Label(window, text=str(values[i])).grid(row=n+2,column=i)
            if number==rand:
                tk.Label(window, text='Your guessed right!').grid(row=16,column=1)
                correct_guess_flag=True
            elif n==12:
                txt='You lose:( The number is: ' +rand
                tk.Label(window, text=txt).grid(row=16,column=1)
                n+=1
        else:
            tk.Label(window, text='Enter a valid number').grid(row=16, column=1)

window=tk.Tk()

n=0
table=list()

window.title("Bulls ans Cows")

tk.Label(window, text='Error Messages:').grid(row=16, column=0)

tk.Label(window, text='Input').grid(row=0,column=0)
entry=tk.Entry(window)
number=entry.get().strip()
entry.grid(row=0,column=1)

tk.Label(window, text='Number').grid(row=2,column=0)
tk.Label(window, text='Bulls').grid(row=2,column=1)
tk.Label(window, text='Cows').grid(row=2,column=2)

submit=tk.Button(window, text="Submit", command=f, bg='white', width=25)
submit.grid(row=1, column=0)

stop =tk.Button(window, text="Exit", command=window.destroy, bg='white', width=25)
stop.grid(row=1,column=1)

window.mainloop()
