n=8
i=3
while i>0: 
    a=int(input("enter a value"))
    if a==n:
        print("you guess the correct value")
        break
    else:
        i=i-1
        print("you have",i,"chances left")
    if i==0:
        print("you lost")
        break