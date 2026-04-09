
import typing

def find_max(arr: typing.List[int]) -> int:
    return max(arr)

numbers = [3, 7, 2, 9, 5]
print(find_max(numbers))
count = 0
while count < 5:
    print(count)
    count += 1
print("Done")
