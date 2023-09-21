class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printlist(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while(temp):
                print(temp.value,end='->')
                temp=temp.next
            print("None")

    def SearchingNode(self):
        x=int(input("Enter the search Nonde="))
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            count=0
            while(temp):
                if(temp.value != x):
                    temp=temp.next
                    count+=1
                else:
                    print("Search node found at=", count , "th index")
                    count=0
                    break
    
            if(count!=0):
                print("not found")

                

l=LinkedList()
l.printlist()

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

l.printlist()

l.SearchingNode()