class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertbegin(self,newNode):
        newNode=Node(newNode)
        newNode.next=self.head
        self.head=newNode
        
    def insertEnd(self,newNode):
        newNode=Node(newNode)
        if self.head is None:
            self.head = newNode
            newNode.next=None
        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next

            temp.next=newNode
            newNode.next=None
    
    def insertAtSpecifiPosition(self,newNode,position):
        newNode=Node(newNode)
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            for i in range(position-1):
                temp=temp.next
            newNode.next=temp.next
            temp.next=newNode

    def insertAfterNode(self,newNode, PrevNode):
        newNode=Node(newNode)
        if PrevNode is None:
            print("Not in list")
        else:
            newNode.next=PrevNode.next
            PrevNode.next=newNode

    def printlist(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            while(temp is not None):
                print(temp.value,end='->')
                temp=temp.next
    
            print("None")

l=LinkedList()
l.insertbegin(10)
l.insertbegin(20)
l.insertbegin(30)
l.insertbegin(40)
l.insertbegin(50)
l.insertbegin(60)
l.printlist()

l.insertEnd(5)
l.printlist()
        
l.insertAtSpecifiPosition(35,3)
l.printlist()


# l.insertAfterNode(6,node)
# l.printlist()