# def quickSort(nums,left,right):
#     def partition(nums,left,right):
#         if left > right :
#             return
#         start = left + 1
#         end = right - 1
#         base = nums[left]
#         while start < end:
#             if ((nums[end] > base) & (start < end)):
#                 end -= 1
#             if ((nums[start] <= base) & (start < end)):
#                 start += 1
#             print nums[end]
#             a = nums[end]
#             b = nums[start]
#             # if (nums[end] <= base) & (nums[start] > base):
#             if (a <= base) & (b > base):
#                 nums[start], nums[end] = nums[end], nums[start]
#                 end -= 1
#                 start += 1
#         nums[left],nums[start] = nums[start],nums[left]
#         return start
#     k = partition(nums,left,right)
#     quickSort(nums,left,k+1)
#     quickSort(nums,k,right)


def quickSort(nums,left,right):
    if left > right:
        return
    def partition(nums,left,right):
        base = nums[0]
        for i in range(left,right):
            if nums[i] > base:

nums = [7,9,4,78,4,6,8,4]
left = 0
right = len(nums)
quickSort(nums,left,right)
print nums

