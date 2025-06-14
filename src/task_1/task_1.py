from collections import defaultdict

def caching_fibonacci():
  cache = defaultdict(list)
  def fib(n: int) -> int:
    if n in cache:
      return cache[n]
    if n <= 1:
      return n

    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]
  return fib

fib = caching_fibonacci()


print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
