# Definition for a binary tree node.
# works in leetcode lol

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        print(root.left.val)
        print(root.right.val)
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    

sol = Solution()
print(sol.maxDepth(root = TreeNode([3,9,20,None,None,15,7])))


# BFS for shortest path only pretty much
#DFS - pop and extend