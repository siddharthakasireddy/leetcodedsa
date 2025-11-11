# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node):
            # returns a tuple: (max_if_robbed, max_if_not_robbed)
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            # If we rob this node, we cannot rob its children
            rob_this = node.val + left[1] + right[1]
            # If we don't rob this node, we can choose to rob or not rob each child
            not_rob_this = max(left[0], left[1]) + max(right[0], right[1])
            return (rob_this, not_rob_this)

        res = dfs(root)
        return max(res[0], res[1])

        