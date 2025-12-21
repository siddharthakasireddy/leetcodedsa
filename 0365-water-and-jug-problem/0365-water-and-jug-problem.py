class Solution(object):
    def canMeasureWater(self, x, y, target):
        if target == 0:
            return True
        if x + y < target:
            return False

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        return target % gcd(x, y) == 0

        