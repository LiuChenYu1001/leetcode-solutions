import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(left, right):
            if left >= right:
                return

            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]
            lt, i, gt = left, left, right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            quick_sort(left, lt - 1)
            quick_sort(gt + 1, right)

        quick_sort(0, len(nums) - 1)

        return nums