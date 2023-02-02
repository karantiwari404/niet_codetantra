def get_input():
    return int(input("Select a Operation 1.Insertion 2.Sorting 3.Display 4.Quit "))


ls = []
while True:
    q = get_input()
    if q == 1:
        ls.append(int(input("Enter a element ")))
    elif q == 2:
        if not ls:
            print("List is Empty")
        ls.sort()

    elif q == 3:
        for i in ls:
            print(i)
    else:
        break