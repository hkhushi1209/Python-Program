def square(n):
    return n*n

# We find square of each number using map()
numbers = (1, 2, 3, 4)
result = map(square, numbers)
print(list(result))