def sum_no_duplicates(lst):
    result = 0
    count = {}
    
    for number in lst:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    
    for number in count:
        if count[number] ==  1:
            result  += number
    return result


print(sum_no_duplicates([3, 4, 3, 6]))
