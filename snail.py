snail_map = [
    [1,2,3],
    [8,9,4],
    [7,6,5]
]

# snail_map =[
#     [1, 2, 3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10, 9, 8, 7],
# ]

def snail(snail_map):
    if not snail_map or not snail_map[0]:
        return []

    length = len(snail_map)
    top, bottom = 0, length - 1
    left, right = 0, length - 1
    result = []

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(snail_map[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(snail_map[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(snail_map[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(snail_map[i][left])
            left += 1

    return result

print(snail(snail_map))