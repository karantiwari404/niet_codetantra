def get_input():
    return int(input("Select an Operation:\n1.Insert\n2.Deletion\n3.Display\n4.Quit\t"))


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head == None:
            print("Linked list is empty")
            return
        n = self.head
        while n:
            print(n.data)
            n = n.next

    def get_length(self):
        c = 0
        n = self.head
        while n:
            c += 1
            n = n.next
            return c

    def insert_at_begining(self):
        data = int(input("Enter Element "))
        node = Node(data, self.head)
        self.head = node

    def remove_at(self):
        index = int(input("Enter a position "))
        if index < 0:
            raise Exception("Invalid Index")
        if index > self.get_length():
            print("Position is more than number of nodes")
            return
        if index == 0:
            self.head = self.head.next
            return
        c = 0
        n = self.head
        while n:
            if c == index - 1:
                n.next = n.next.next
                break
            n = n.next
            c += 1


ll = LinkedList()
while True:
    q = get_input()
    if q == 1:
        ll.insert_at_begining()
    elif q == 2:
        ll.remove_at()
    elif q == 3:
        ll.print_ll()
    elif q == 4:
        break
    else:
        print("Invalid Option!!!")