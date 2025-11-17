class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # Use a stack, push items in reverse order
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        # hasNext() ensures top is always an integer
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        # Flatten until the top is an integer
        while self.stack:
            top = self.stack[-1]

            if top.isInteger():
                return True

            # Otherwise it is a list → expand it
            self.stack.pop()
            lst = top.getList()

            # Push elements in reverse so they appear in correct order
            for item in lst[::-1]:
                self.stack.append(item)

        return False
