class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = list()
        temp = list()
        self.helper(nums, ans, temp)
        return ans

    def helper(self, nums, ans, temp):
        if len(temp) == len(nums):
            ans.append(temp.copy())

        for i in range(0, len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            self.helper(nums, ans, temp)
            temp.pop()
