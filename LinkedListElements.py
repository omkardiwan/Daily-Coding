#Code to print all the elements in a linkedlist

class Node:
    def __init__(self, data):
        self.data =  data
        self.next = None
        
     
ten = Node(10)
head = ten 
twenty = Node(20)
thirty = Node(30)
forty = Node(40)

ten.next = twenty
twenty.next = thirty
thirty.next = forty
forty.next = None

Current = head

while(Current.next != None):
    print (Current.data)
    Current = Current.next
