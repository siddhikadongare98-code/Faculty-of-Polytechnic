num = 10

unum = int(input("Guess a number between 1 to 20: "))

if unum < num:
    print("Low")
elif unum > num:
    print("High")
else:
    print("Correct")
#problem
num=10
unum=0
while unum!=num:
    unum=int(input("guess a num bet 1 to 10="))
    if(unum==10):
        print("correct guess")
    else:
        print("incorrect guess")
        
