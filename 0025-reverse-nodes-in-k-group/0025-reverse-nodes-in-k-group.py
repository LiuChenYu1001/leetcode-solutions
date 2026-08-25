# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        pre = dummy

        while True:
            node = pre
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next

            cur = pre.next
            for _ in range(k-1):
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt

            pre = cur

        return dummy.next