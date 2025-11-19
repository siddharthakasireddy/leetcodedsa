class Solution(object):
    def deserialize(self, s):
        # If s is just a number (no list), return it directly
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ""
        negative = False

        for char in s:
            if char == '-':
                negative = True
            
            elif char.isdigit():
                num += char

            elif char == '[':
                stack.append(NestedInteger())

            elif char in ',]':
                # If we have built a number, convert and add it
                if num:
                    val = int(num)
                    if negative:
                        val = -val
                    stack[-1].add(NestedInteger(val))
                    num = ""
                    negative = False

                if char == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)

        return stack[0]

        