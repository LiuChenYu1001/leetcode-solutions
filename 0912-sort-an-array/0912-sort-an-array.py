class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def heapify(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and nums[left] > nums[i]:
                largest = left

            if right < n and nums[right] > nums[largest]:
                largest = right

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)

        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for j in range(n - 1, 0, -1):
            nums[j], nums[0] = nums[0], nums[j]
            heapify(j, 0)

        return nums