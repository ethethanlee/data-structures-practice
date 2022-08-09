# Singularly Linked List:
# class Node:
#     def __init__(self, item=None):
#         self.item = item
#         self.next = None
 
# class LinkedList:
#     def __init__(self):
#         self.head = None

# def LLprint(linked_list):
#     temp = []
#     node = linked_list.head
#     while node: 
#         temp.append(str(node.item))
#         node = node.next
#     print(' -> '.join(map(str, temp)))









# Doubly:
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.prev = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def LLprint(linked_list):
    temp = []
    node = linked_list.head
    for i in range(4): ## while node: only works if not circular
        temp.append(str(node.item))
        node = node.next
    print(' <-> '.join(map(str, temp)))
    if (linked_list.head.prev == linked_list.tail):
        print ('This is a circular linked list!')

list1 = LinkedList()
e1 = Node("Mon")
list1.head = e1
e2 = Node("Tue")
e3 = Node("Wed")
list1.tail = e3
# Link first Node to second node
list1.head.next = e2
e2.prev = list1.head
 
# Link second Node to third node
e2.next = e3
e3.prev = e2

e3.next = e1
e1.prev = e3

e1.item = 1
e2.item = 2
e3.item = 3

LLprint(list1)


