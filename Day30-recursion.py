
def factorial(n):
  if n== 0 or n==1:
    return 1
  else:
    return n * factorial(n-1)


print(factorial(3))
print(factorial(4))
print(factorial(5))


def feb(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
  return n + feb(n-1) + feb(n-2)
  