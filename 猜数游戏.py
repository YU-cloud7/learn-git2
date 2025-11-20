n=int (input().strip())
low=1
high=99
count=0
guesses=[]
while True:
    guess=(low+high)//2
    guesses.append(guess)
    count+=1
    if guess==n:
        break
    elif guess>n:
        high=guess-1
    else:
        low=guess+1
for g in guesses:
    print(g)
print(count)