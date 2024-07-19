def digital_root(n:str):
    result = 0
    numbers = []
    for i in str(n):
        numbers.append(int(i))
    result = sum(numbers)
    if result >= 10:
        return digital_root(result)
    return result

print(digital_root(1))
