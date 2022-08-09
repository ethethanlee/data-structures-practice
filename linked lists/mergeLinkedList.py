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
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node1 = list1.head
        node2 = list2.head
        output = LinkedList
        temphead = Node(None)
        output.head = temphead
        temp = temphead
        while node1 and node2:
            if node1.item <= node2.item:
                temp.next = node1
                temp = node1
                node1 = node1.next
            elif node2.item < node1.item:
                temp.next = node2
                temp = node2
                node2 = node2.next
        while node1:
            temp.next = node1
            temp = node1
            node1 = node1.next
        while node2:
            temp.next = node2
            temp = node2
            node2 = node2.next
        output.head = temphead.next
        temphead.next = None
        return output
                







sol = Solution()
list1 = LinkedList()
e1 = Node(1)
list1.head = e1
e2 = Node(2)
e1.next = e2
e3 = Node(3)
e2.next = e3 


list2 = LinkedList()
e1 = Node(1)
list2.head = e1
e2 = Node(2)
e1.next = e2
e4 = Node(4)
e3.next = e4
e5 = Node(5)
e4.next = e5

LLprint(sol.mergeTwoLists(list1, list2))