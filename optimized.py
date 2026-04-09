
import typing

def find_maximum(arr: typing.List[int]) -> int:
    try:
        return max(arr)
    except ValueError as e:
        print("Empty list provided: ", str(e))
        raise

numbers = [3, 7, 2, 9, 5]
print(find_maximum(numbers))
count = 0
while count < 5:
    print(count)
    count += 1
print("Done")
