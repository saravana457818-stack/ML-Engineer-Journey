max=int(input("enter the max value:"))
odd=[]
for i in range(1,max):
    if i%2!=0:
        odd.append(i)
        print(odd)
    else:
        
        print("over and out")
