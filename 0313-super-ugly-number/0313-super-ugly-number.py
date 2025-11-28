class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        k = len(primes)
        ugly = [1] * n                    # dp array of ugly numbers
        idx = [0] * k                     # pointers for each prime
        next_mult = primes[:]             # next candidates

        for i in range(1, n):
            # next ugly number is the minimum among candidates
            next_ugly = min(next_mult)
            ugly[i] = next_ugly

            # update pointers for all primes that match next_ugly
            for j in range(k):
                if next_mult[j] == next_ugly:
                    idx[j] += 1
                    next_mult[j] = ugly[idx[j]] * primes[j]

        return ugly[-1]

        