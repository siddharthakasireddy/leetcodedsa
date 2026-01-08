class Solution(object):
    def flatten(self, head):
        if not head:
            return head

        def dfs(node):
            curr = node
            last = None

            while curr:
                nxt = curr.next

                # If current node has a child
                if curr.child:
                    # Flatten the child list
                    child_head = curr.child
                    child_tail = dfs(child_head)

                    # Connect curr -> child
                    curr.next = child_head
                    child_head.prev = curr

                    # Connect child_tail -> nxt
                    if nxt:
                        child_tail.next = nxt
                        nxt.prev = child_tail

                    # Remove child pointer
                    curr.child = None

                    last = child_tail
                    curr = child_tail
                else:
                    last = curr

                curr = curr.next

            return last

        dfs(head)
        return head

        