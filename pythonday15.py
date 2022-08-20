class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        self.head = head
        self.data = data
        if head == None:
            new_node = Node(data)
            head = new_node
            return head
        store_head = head
        while(head.next is not None):
            head = head.next
        new_node = Node(data)
        head.next = new_node
        head = store_head
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	 