# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addNodes(n1, n2, carry):
            if not n1 and not n2 and carry == 0:
                return None
            val1 = n1.val if n1 else 0
            val2 = n2.val if n2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            node = ListNode(total % 10)
            node.next = addNodes(n1.next if n1 else None, n2.next if n2 else None, carry)
            return node

        return addNodes(l1, l2, 0)
