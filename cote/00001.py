nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)

##

for i, n in enumerate(nums):
    complement = target - n

    if complement in nums[i+1:]:
        print(nums.index(n), nums[i+1:].index(complement) + (i+1))

##

nums_dict = {}
for i, num in enumerate(nums):
    nums_dict[num] = i

for i, num in enumerate(nums):
    if target - num in nums_dict and i != nums_dict[target - num]:
        print(i, nums_dict[target-num])

##

nums_dict = {}
for i, num in enumerate(nums):
    if target - num in nums_dict:
        print(i, nums_dict[target-num])
    nums_dict[num] = i