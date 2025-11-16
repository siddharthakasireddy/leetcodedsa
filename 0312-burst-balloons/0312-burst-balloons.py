class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        
        dp = [[0] * n for _ in range(n)]
        
        # len is the length of the interval
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                # try bursting k last between left and right
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][k] + nums[left] * nums[k] * nums[right] + dp[k][right]
                    )
        
        return dp[0][n - 1]

        