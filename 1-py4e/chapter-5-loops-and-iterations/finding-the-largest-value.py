print('Welcome!')

# largest number so far
largest_so_far = -1

print('\nBefore', largest_so_far)

# looping through a array of numbers
for num in [9, 41, 12, 3, 74, 15, 101]:
    if num > largest_so_far:
        largest_so_far = num
    print(largest_so_far, num)

print('After', largest_so_far)