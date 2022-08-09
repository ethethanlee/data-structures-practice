# Definition for singly-linked list.
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        # self.prev = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None

def LLprint(linked_list):
    temp = []
    node = linked_list.head
    while node: ## while node: only works if not circular
        temp.append(str(node.item))
        node = node.next
    print(' -> '.join(map(str, temp)))
    # if (linked_list.head.prev == linked_list.tail):
    #     print ('This is a circular linked list!')

class Solution(object):
    def reverseList(self, ll):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = Node(None)
        current = ll.head
        # print(current.item)
        temp = Node(None)
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        newList = LinkedList
        newList.head = prev
        return newList
            



sol = Solution()
list1 = LinkedList()
e1 = Node(1)
list1.head = e1
e2 = Node(2)
e1.next = e2
e3 = Node(3)
e2.next = e3
e4 = Node(4)
e3.next = e4
e5 = Node(5)
e4.next = e5

LLprint(sol.reverseList(list1))