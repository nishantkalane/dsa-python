from Scripts.activate_this import prev_length


class ListNode: #creating our class for linked list
    def __init__(self, val=0, next=None):
        self.val =val #assigning value
        self.next =next #assigning next box address

node1 =ListNode(10)
node2= ListNode(20)
node3=ListNode(30)
node4=ListNode(40)

node1.next =node2
node2.next=node3
node3.next=node4

#Traversing the list
head=node1
while head:
    print(head.val)
    head= head.next
print()

#find middle

head=node1
def find_middle(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow
middle=find_middle(head)
print(middle.val)


print()
#reversing
def reverse_linked_list(head):

    prev=None
    while head:
        nxt=head.next #Save
        head.next=prev #reverse
        prev=head #mover previous
        head =nxt #move head
    return prev

head= (reverse_linked_list(node1))

while head:
    print(head.val)
    head=head.next





