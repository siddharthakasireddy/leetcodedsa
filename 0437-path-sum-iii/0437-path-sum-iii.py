class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        prefixSumCount = {0: 1}
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum += node.val
            
            # Count paths ending at this node with sum = targetSum
            count = prefixSumCount.get(current_sum - targetSum, 0)
            
            # Update prefix sum count
            prefixSumCount[current_sum] = prefixSumCount.get(current_sum, 0) + 1
            
            # Continue DFS
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            # Backtrack
            prefixSumCount[current_sum] -= 1
            
            return count
        
        return dfs(root, 0)

        