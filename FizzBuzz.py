result = []
for i in range(1, 101):
    result.append("Fizz"*(i % 3 == 0) + "Buzz"*(i % 5 == 0) or i)
#     result.append([i, "Buzz", "Fizz", "FizzBuzz"][2*(i % 3 == 0) + (i % 5 == 0)])

print(result)


