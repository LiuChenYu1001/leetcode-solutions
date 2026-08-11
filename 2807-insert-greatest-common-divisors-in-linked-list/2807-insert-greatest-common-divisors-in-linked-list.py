# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            a = cur.val
            b = cur.next.val
            num = gcd(a, b)

            new_node = ListNode(num)
            new_node.next = cur.next
            cur.next = new_node


            cur = new_node.next

        return head