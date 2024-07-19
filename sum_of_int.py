def rearrange(nums):
    nums = sorted(nums, key=lambda x: x[0])
    tracking_arr = sorted(nums, key=lambda x: x[0])
    removing_arr = sorted(nums, key=lambda x: x[0])
    arranged_arr = []
    try_recursion: list = []
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
            # mixed_arr = [lowest_num, max(highest_num, arr[1])]
            new_arr.append(mixed_arr)
            # print(f'removing these arrs {arr} and {nums[i+1]}')
            removing_arr.remove(nums[i + 1])
            removing_arr.remove(arr)
        # print(f'removing arr is {removing_arr}')
    arranged_arr = new_arr + removing_arr
    print(arranged_arr , try_recursion)
    if arranged_arr == try_recursion:
        return arranged_arr
    try:
        print('In try catch')
        try_recursion = rearrange(arranged_arr)
        if try_recursion == arranged_arr:
            return arranged_arr
        else:
            return rearrange(try_recursion)
        
    except:
        return arranged_arr
    
        
print(rearrange([
    [1, 2],
   [6, 10],
   [11, 15]
]))


# print(rearrange([
#    [1, 5],
#    [10, 20],
#    [1, 6],
#    [16, 19],
#    [5, 11]
# ]))

