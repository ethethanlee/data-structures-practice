def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    index = headA
    ring = headB
    
    while index != ring:
        if not index:
            index = headB
        else:
            index = index.next
        
        if not ring:
            ring = headA
        else:
            ring = ring.next
            
    return index

#leetcode 160