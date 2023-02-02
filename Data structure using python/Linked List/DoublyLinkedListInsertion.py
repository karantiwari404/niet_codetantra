def get_input():
    return int(input("Select Opertion\n1.Insertion\n2.Display\n3.Quit\t"))


ls = []
while True:
    q = get_input()
    if q == 1:
        ls.append(int(input("enter element ")))
    elif q == 2:
        print("Adding a node to the end of the list: ")
        for i in ls:
            print(i)
    else:
        break