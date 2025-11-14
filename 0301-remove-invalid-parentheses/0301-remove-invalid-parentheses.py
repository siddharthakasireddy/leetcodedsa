class Solution(object):
    def removeInvalidParentheses(self, s):
        from collections import deque
        
        def isValid(st):
            count = 0
            for ch in st:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                if count < 0:     # More ')' than '('
                    return False
            return count == 0      # Balanced
        
        queue = deque([s])
        visited = set([s])
        result = []
        found = False
        
        while queue:
            curr = queue.popleft()
            
            if isValid(curr):
                result.append(curr)
                found = True   # Found minimum-removal valid level
            
            if found:
                continue  # Don’t generate deeper levels once minimum is found
            
            for i in range(len(curr)):
                if curr[i] not in "()":
                    continue
                nxt = curr[:i] + curr[i+1:]
                
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return result

        