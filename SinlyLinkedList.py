class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class singlyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = newNode
            temp.next = self.head
            self.head = temp

    def insertAtI(self, data, i):
        # Here the i value represent the position to insert Node.Ex: 1 2 3 4, value of i between Node 2 and Node 3 is 2.
        newNode = Node(data)
        if i == 0:
            self.insertAtBeginning(data)
            return
        if i > self.countLength() + 1:
            print("Invalid Position")
            return
        if i == self.countLength():
            self.insertAtEnd(data)
            return
        temp = self.head
        count = 0
        while temp is not None and count != i - 1:
            count += 1
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode

    def countLength(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def deletionAtEnd(self):
        temp = self.head
        if self.head is None:
            print("No Node Present")
            return
        if temp.next is None:
            print("One Node Present")
            self.head = None
            return
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def deletionAtBeginning(self):
        temp = self.head
        if self.head is None:
            print("No Node Present")
            return
        if temp.next is None:
            print("One Node Present")
            return
        self.head = temp.next

    def deletionAtI(self, i):
        # Here the i value represent the node number. Ex: 1 2 3 4, Here i value of Node 2 is 2.
        if i == 1:
            self.deletionAtBeginning()
            return
        if i == self.countLength():
            self.deletionAtEnd()
            return
        if i > self.countLength() or i == 0:
            print("Invalid Position")
            return
        temp = self.head
        count = 0
        while temp.next is not None and count != i - 2:
            count += 1
            temp = temp.next
        temp.next = temp.next.next

    def printSinglyLinkedList(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()



