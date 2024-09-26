nums = list(map(int, input().split()))

original_nums = []

for i in range(len(nums)):
    original_nums.append(nums[i])

for i in range(len(nums) - 1):
    for j in range(len(nums) - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

for i in range(len(nums)):
    print(nums[i])
print()
for j in range(len(original_nums)):
    print(original_nums[j])
