class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums1)
        nums1.sort()
        order = sorted(range(n), key = lambda i: nums2[i], reverse = True)
        left, right = 0, n - 1
        ans = [0] * n

        for i in order:
            if nums1[right] > nums2[i]:
                ans[i] = nums1[right]
                right -= 1
            else:
                ans[i] = nums1[left]
                left += 1

        return ans