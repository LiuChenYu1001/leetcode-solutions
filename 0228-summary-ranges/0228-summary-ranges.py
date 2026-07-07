class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        tem = [nums[0]]
        ans = []

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if len(tem) == 1:
                    ans.append(str(tem[0]))

                else:
                    num1 = str(tem[0])
                    num2 = str(tem[-1])
                    ans.append(f"{num1}->{num2}")

                tem = [nums[i]]

            else:
                tem.append(nums[i])

        if len(tem) == 1:
            ans.append(str(tem[0]))
        else:
            num1 = str(tem[0])
            num2 = str(tem[-1])
            ans.append(f"{num1}->{num2}")

        return ans