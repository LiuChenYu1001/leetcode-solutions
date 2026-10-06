import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def quickselect(left, right):
            if left == right:
                return nums[left]

            pivot = nums[random.randint(left, right)]
            lt = mid = left
            gt = right

            while mid <= gt:
                if nums[mid] < pivot:
                    nums[lt], nums[mid] = nums[mid], nums[lt]
                    lt += 1
                    mid += 1
                elif nums[mid] > pivot:
                    nums[gt], nums[mid] = nums[mid], nums[gt]
                    gt -= 1
                else:
                    mid += 1

            if k < lt:
                return quickselect(left, lt - 1)
            elif k > gt:
                return quickselect(gt + 1, right)
            else:
                return nums[k]

        return quickselect(0, len(nums) - 1)