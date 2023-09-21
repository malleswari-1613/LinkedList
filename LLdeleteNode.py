class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head = None


    def printList(self):
        if self.head is None:
            print("empty List")
        else:
            temp=self.head
            while(temp):
                print(temp.value, end='->')
                temp=temp.next
            print("None")

    def deleteBeg(self):
        if self.head is None:
            print("No nodes are there in list")
        else:
            temp=self.head
            self.head=temp.next
            temp=None

    def deleteEnd(self):
        if self.head is None:
            print("No nodes are there in list")
        else:
            temp=self.head
            while(temp.next.next is not None):
                temp=temp.next
            temp.next=None

    def deleteAfterNode(self,PrevNode):
        if PrevNode is None:
            print("Node is not there")
        else:
            temp=PrevNode.next
            PrevNode.next=PrevNode.next.next
            temp.next=None
            temp=None

l=LinkedList()
l.head=Node(5)
one=Node(10)
two=Node(20)
three=Node(30)
four=Node(40)
l.head.next=one
one.next=two
two.next=three
three.next=four
four.next=None

l.printList()

l.deleteBeg()
l.printList()

l.deleteEnd()
l.printList()

l.deleteAfterNode(one)
l.printList()