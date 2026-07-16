class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k == 0:
            return

        start = 0
        move = 0

        while move < n:
            cur = start
            prev = nums[cur]

            while True:
                nxt = (cur + k) % n
                prev, nums[nxt] = nums[nxt], prev
                cur = nxt
                move += 1

                if nxt == start:
                    break

            start += 1