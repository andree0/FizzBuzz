result = []
for i in range(1, 101):
    result.append("Fizz"*(i % 3 == 0) + "Buzz"*(i % 5 == 0) or i)

print(result)
