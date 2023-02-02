def get_input():
    return int(input("Select a option: 1.Insertion 2.Reversal 3.Display 4.Quit "))


ls = []
while True:
    q = get_input()
    if q == 1:
        ls.append(int(input("Enter number ")))
    elif q == 2:
        ls = ls[::-1]
    elif q == 3:
        for i in ls[::-1]:
            print(i)
    else:
        break