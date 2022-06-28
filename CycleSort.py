nums = [2, 3, 1, 5, 4]
i = 0
correct=0
while i < len(nums):
    correct = nums[i] - 1
    if nums[i] != nums[correct]:
        def swap():
            temp = nums[correct]
            nums[correct] = nums[i]
            nums[i] = temp


        swap()
    else:
        i += 1

print(nums)
