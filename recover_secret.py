def recoverSecret(triplets):
    def intializer(triplets):
        order_arr = []
        for arr in triplets:
            for letter in arr:
                if letter not in order_arr:
                    order_arr.append(letter)
        return order_arr
    def is_order_correct(triplets, order_arr):
        left, mid, right = triplets
        return order_arr.index(left) < order_arr.index(mid) < order_arr.index(right)      
    def update_order_arr(triplets, order_arr):
        left, mid, right = triplets
        left_index = order_arr.index(left)
        mid_index = order_arr.index(mid)
        right_index = order_arr.index(right)
            
        if left_index > right_index:
            order_arr[left_index], order_arr[right_index] = order_arr[right_index], order_arr[left_index]
            left_index, right_index = right_index, left_index
        if mid_index > right_index:
            order_arr[mid_index], order_arr[right_index] = order_arr[right_index], order_arr[mid_index]
            mid_index, right_index = right_index, mid_index
        if mid_index < left_index: 
            order_arr[mid_index], order_arr[left_index] = order_arr[left_index], order_arr[mid_index]
            mid_index, left_index = left_index, mid_index 
        return order_arr
    order_arr = intializer(triplets)
    is_changed = True
    while is_changed:
        is_changed = False
        for triplet in triplets:
            if not is_order_correct(triplet, order_arr):
                order_arr = update_order_arr(triplet, order_arr)
                is_changed = True
    return ''.join(order_arr)
            
triplets = [
    ['h', 'a', 'c'],
    ['h', 'a', 'k'],
    ['h', 'k', 'r'],
    ['h', 'c', 'e'],
    ['h', 'c', 'r'],
    ['a', 'e', 'r'],
    ['a', 'k', 'r'],
    ['c', 'e', 'r'],
    ['c', 'k', 'e']
]


print(recoverSecret(triplets))
