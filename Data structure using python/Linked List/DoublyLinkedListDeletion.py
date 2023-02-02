def get_input():
    return int(input("Select Opertion 1.Insertion 2.DeletefromStart 3.Display 4.Quit "))


ls = []
while True:
    q = get_input()
    if q == 1:
        ls.append(int(input("Enter element ")))
    elif q == 2:
        if not ls:
            print("List is empty")
            continue
        ls.pop(0)
    elif q == 3:
        if not ls:
            print("List is empty")
            continue
        for i in ls:
            print(i)
    elif q == 4:
        break
    else:
        print("Invalid Option!!!")