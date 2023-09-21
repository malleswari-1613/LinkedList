class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self,newNode):
        newNode=Node(newNode)
        if self.head is None:
            self.head=newNode
            newNode.next = None
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=newNode
            newNode.next=None

    def printList(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            while(temp):
                print(temp.value, end='->')
                temp=temp.next
            print("None")

    def reverseLL(self):
        if self.head is None:
            print("empty list")
        else:
            prev=None
            current=self.head
            while(current):
                next=current.next
                current.next=prev
                prev=current
                current=next
            self.head=prev     


l=LinkedList()
l.printList()

l.insertNode(10)
l.insertNode(20)
l.insertNode(30)
l.insertNode(40)
l.insertNode(50)
l.insertNode(60)

l.printList()

l.reverseLL()
l.printList()