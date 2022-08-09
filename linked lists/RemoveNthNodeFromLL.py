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

list1 = LinkedList()
e1 = Node(1)
list1.head = e1
e2 = Node(2)
e1.next = e2
# e3 = Node(3)
# e2.next = e3
# e4 = Node(4)
# e3.next = e4
# e5 = Node(5)
# e4.next = e5

class Solution(object):
    def removeNthFromEnd2n(self, list1, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = -1
        temp = list1.head
        while temp:
            temp.next = temp.next
            temp = temp.next
            i+=1
        temp = list1.head
        LLprint(list1)
        while i>(n+1):
            temp.next = temp.next
            temp = temp.next
            i-=1
        temp.next = temp.next.next
        temp = temp.next.next
        return list1
    

    def removeNthFromEnd(self, list1, n):
        i = 0
        fast = list1.head
        slow = list1.head
        while n > i:
            fast = fast.next
            if not fast:
                return list1.head.next
            i+=1
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return list1


sol = Solution()
LLprint(sol.removeNthFromEnd(list1, 1))