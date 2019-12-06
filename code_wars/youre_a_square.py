def is_square(n):
  for i in range(0, n):
        square = i * i
        if square > n or n < 0: return False
        if square == n: return True

print(is_square(0))