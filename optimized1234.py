
import random

def setup_data(items: list = []) -> list:
    items.append(random.randint(0, 10))
    return items

data  = setup_data()
for i in range(5):
    if i != 2:
        print(i)
    else:
        continue

def fail_function(a: int, b: str) -> int:
    result = a + int(b)
    return result
result  = fail_function(10, "5")
print(result)
