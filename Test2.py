
1  def reverse_string(s: str) -> str:
2      return s[::-1]
3
4  text = "12345"
5
6  print("Reversed:", reverse_string(text))
7
8  def square(n: int) -> int:
9      try:
10          return n ** 2
11      except TypeError:
12          return "Input must be an integer"
13
14  result = square(5)
15  print(result)
