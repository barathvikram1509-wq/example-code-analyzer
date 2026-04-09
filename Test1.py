def find_max(arr):
    max_val = arr[0]
    for i in arr:
        if arr > max_val:
            max_val = i
    return max_val

numbers = [3, 7, 2, 9, 5]

print(find_max(numbers))

count = 0
while count < 5:
    print(count)

print("Done")
