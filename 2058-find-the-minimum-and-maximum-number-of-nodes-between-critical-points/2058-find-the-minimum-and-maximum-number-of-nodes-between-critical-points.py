# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        cur = head.next
        index = 1
        pre_cri = -1
        first_cri = -1
        min_dist = float("inf")

        while cur.next:
            nxt = cur.next

            if (prev.val < cur.val > nxt.val) or (prev.val > cur.val < nxt.val):
                if first_cri == -1:
                    first_cri = index
                else:
                    min_dist = min(min_dist, index - prev_cri)

                prev_cri = index

            prev = cur
            cur = cur.next
            index += 1

        if min_dist == float("inf"):
            return [-1, -1]

        max_dist = prev_cri - first_cri

        return [min_dist, max_dist]