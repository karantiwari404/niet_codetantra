def get_input():
    return int(input("Select Operation\n1.Insertion\n2.Updation\n3.Display\n4.Quit\t"))


ls = []
while True:
    q = get_input()
    if q == 1:
        ls.append(int(input("Enter element ")))
    elif q == 2:
        key = int(input("Enter the index to update "))
        val = int(input("Enter a value to update "))
        ls[-key - 1] = val
    elif q == 3:
        for i in ls[::-1]:
            print(i)
    else:
        break