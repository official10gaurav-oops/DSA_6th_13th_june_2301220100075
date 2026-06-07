nums = [5, 9, 75, 13, 2, 58]
n = len(nums)

# Sorting using nested loops (Selection Sort style)
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print("Mini", nums[0])
print("Maxi", nums[n - 1])