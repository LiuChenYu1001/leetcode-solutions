# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(next = head)
        slow = dummy
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        pre = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        ans = 0
        first = head
        second = pre
        while second:
            ans = max(ans, first.val + second.val)
            first = first.next
            second = second.next

        return ans