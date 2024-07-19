def rearrange(nums, recursed = False):
    nums = sorted(nums, key=lambda x: x[0])
    tracking_arr = sorted(nums, key=lambda x: x[0])
    removing_arr = sorted(nums, key=lambda x: x[0])
    arranged_arr = []
    try_recursion = []
    new_arr = []
    if len(nums) >=2:
        highest_num = nums[1][1]
    else:
        return nums
    for i, arr in enumerate(nums):
        if not removing_arr:
            break
        lowest_num = min(arr[0] for arr in removing_arr)
        if i < len(nums) - 1:
            highest_num = tracking_arr[i][1]
            checking_num = tracking_arr[i+1][0]
        else:
            break
        if arr not in removing_arr:
            continue
        if lowest_num <= checking_num and checking_num <= highest_num:          
            mixed_arr = [lowest_num, max(highest_num, tracking_arr[i + 1][1])]
            new_arr.append(mixed_arr)
            removing_arr.remove(nums[i + 1])
            removing_arr.remove(arr)
    arranged_arr = new_arr + removing_arr
    if recursed:
        return arranged_arr
    try:
        try_recursion = rearrange(arranged_arr, recursed= True)
        if try_recursion == arranged_arr:
            return arranged_arr
        else:
            return rearrange(try_recursion, recursed= False)
        
    except:
        return arranged_arr
def sum_of_intervals(intervals):
    result = 0
    new_arr = rearrange(intervals)
    for arr in new_arr:
        difference = lambda x, y : y - x
        result += difference(arr[0], arr[1])
    return result  
# nums = [
#     [1, 5],
#     [10, 20],
#     [1, 6],
#     [16, 19],
#     [5, 11]
# ]
# print(sum_of_intervals(nums))

print(rearrange([
    [1, 2],
   [6, 10],
   [11, 15]
]))