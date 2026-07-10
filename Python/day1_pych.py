students=[]
while True:
    print("1:add","2:display","3:search","4:exit")
    options=int(input("options:"))
    if options == 1:
        name=input("name:")
        students.append(name)
    elif options ==2:
        print(students)
    elif options==3:
        name=input("name:")
        if name in students:
            print("found")
        else:
            print("not found")
    elif options==4:
        print("thank you")
        break
    
