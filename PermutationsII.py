'''
class solution:
def permuteUnique(self, nums):
        arr = []
        self.permute(0, nums, arr)
        return arr

    def permute(self, idx, nums, arr):
        if idx == len(nums) and nums not in arr:
            arr.append(list(nums))
            return

        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            self.permute(idx + 1, nums, arr)
            nums[i], nums[idx] = nums[idx], nums[i]
'''
from collections import Counter


class Solution:
    def permuteUnique(self, nums):
        ans = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                ans.append(list(comb))

            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    counter[num] += 1
                    comb.pop()

        backtrack([], Counter(nums))
        return ans
