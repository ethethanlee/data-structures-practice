# Singularly Linked List:
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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        