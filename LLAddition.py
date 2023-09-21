class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

def push(head,new_node):
    new_node=Node(new_node)
    new_node.next=head
    head=new_node
    return head

def print_list(head):
    i=head
    while i:
        print(i.value,end='->')
        i=i.next
    print("None")


def addlists(l1,l2):
    dummy=Node(0)

    cur = dummy
    carry=0

    while l1 or l2 or carry:
        v1=l1.value if l1 else 0  
        v2=l2.value if l2 else 0

        val=v1+v2+carry

        carry=val//10
        val=val%10

        cur.next=Node(val)
        cur=cur.next

        l1=l1.next if l1 else None
        l2=l2.next if l2 else None

    dummy=dummy.next
    return dummy

    # while l1 or l2:
    #     sum_list=0
    #     if l1:
    #         sum_list += l1.value
    #         l1=l1.next
    #     if l2:
    #         sum_list += l2.value
    #         l2=l2.next

    #     sum_list += carry

    #     cur.next = Node(sum_list % 10)
    #     cur=cur.next

    #     carry=sum_list // 10

    # if carry:
    #     cur.next = Node(carry)

    # return dummy.next


l1=None
l1=push(l1,1)
l1=push(l1,5)

print_list(l1)

l2=None
l2=push(l2,3)
l2=push(l2,9)
l2=push(l2,7)
print_list(l2)

sum_lists=addlists(l1,l2)

print_list(sum_lists)
