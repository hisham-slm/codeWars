def recoverSecret(triplets):
    def initialize_order_arr(triplets):
        order_arr = []
        for triplet in triplets:
            for letter in triplet:
                if letter not in order_arr:
                    order_arr.append(letter)
        return order_arr

    def is_order_correct(triplet, order_arr):
        left, mid, right = triplet
        return order_arr.index(left) < order_arr.index(mid) < order_arr.index(right)

    def update_order_arr(triplet, order_arr):
        left, mid, right = triplet
        left_index, mid_index, right_index = order_arr.index(left), order_arr.index(mid), order_arr.index(right)
        
        if left_index > mid_index:
            order_arr[left_index], order_arr[mid_index] = order_arr[mid_index], order_arr[left_index]
            left_index, mid_index = mid_index, left_index

        if mid_index > right_index:
            order_arr[mid_index], order_arr[right_index] = order_arr[right_index], order_arr[mid_index]
            mid_index, right_index = right_index, mid_index

        if left_index > mid_index:
            order_arr[left_index], order_arr[mid_index] = order_arr[mid_index], order_arr[left_index]
            left_index, mid_index = mid_index, left_index

        return order_arr

    order_arr = initialize_order_arr(triplets)
    
    is_changed = True
    while is_changed:
        is_changed = False
        for triplet in triplets:
            if not is_order_correct(triplet, order_arr):
                order_arr = update_order_arr(triplet, order_arr)
                is_changed = True
    
    return ''.join(order_arr)

# Example usage:
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]
print(recoverSecret(triplets))
