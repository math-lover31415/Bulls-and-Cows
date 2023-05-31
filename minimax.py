import itertools
from random import choice
from command_line import bulls_and_cows


#find number of elements eliminated from S if guess is the guess made and key is the hidden key that it is compared to
def find_score(guess,key, S):
    l=sum(1 for x in S if bulls_and_cows(guess,key)==bulls_and_cows(guess,x))
    return len(S)-l

#find the guess in T that would eliminate the most numbers from S in the worst case scenario
def minmax(T,S):
    memo=dict()
    max=0
    out=list()
    for guess in T:
        min=len(S)
        for key in S:
            if (guess,key) in memo:
                score=memo[(guess,key)]
            else:
                score=find_score(guess,key,S)
                memo[(guess,key)]=score
            if score<min:
                min=score
        if min>max:
            max=min
            out=list()
        if min<max:
            continue
        out.append(guess)
    return out

optimal="0123"

T = set(''.join(p) for p in itertools.permutations([str(n) for n in range(10)],r=4))
S=T

while len(S)>=2:
    print("The guess to be made is: %s" % (optimal))
    bull_num=int(input("Enter number of Bulls:"))
    cow_num=int(input("Enter number of Cows:"))
    S=set(filter(lambda x:bulls_and_cows(optimal,x)==(bull_num,cow_num),S))
    T.discard(optimal)
    optimal_list=minmax(T,S)
    print(optimal_list)
    optimal=choice(optimal_list)
print(S)
