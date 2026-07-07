# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        a, b = l1, l2
        carry = 0
        cur = dummy

        while a or b or carry:
            val = carry

            if a:
                val += a.val
                a = a.next

            if b:
                val += b.val
                b = b.next

            carry = val // 10

            cur.next = ListNode(val % 10)
            cur = cur.next

        return dummy.next