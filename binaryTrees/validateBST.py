# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root, maxi = float('inf'), mini = float('-inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val >= maxi or root.val <= mini:
            return False
        return self.isValidBST(root.left, min(root.val,maxi), mini) and self.isValidBST(root.right, maxi, max(root.val,mini))


        