class Solution(object):
    def addOperators(self, num, target):
        res = []
        n = len(num)

        def backtrack(index, expr, value, last):
            # index: current position in num
            # expr: current expression string
            # value: evaluated value so far
            # last: last multiplied value (for handling '*')
            
            if index == n:
                if value == target:
                    res.append(expr)
                return
            
            for i in range(index, n):
                # avoid numbers with leading zero
                if i > index and num[index] == '0':
                    break

                curr_str = num[index:i+1]
                curr = int(curr_str)

                # If this is the first number, just start the expression
                if index == 0:
                    backtrack(i+1, curr_str, curr, curr)
                else:
                    # '+'
                    backtrack(i+1, expr + "+" + curr_str, value + curr, curr)
                    # '-'
                    backtrack(i+1, expr + "-" + curr_str, value - curr, -curr)
                    # '*'
                    backtrack(i+1, expr + "*" + curr_str, value - last + last * curr, last * curr)

        backtrack(0, "", 0, 0)
        return res

        