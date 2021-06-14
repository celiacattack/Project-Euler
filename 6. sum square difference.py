#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sum_squares = 0

square_sum = 0

for i in range(1,101):
    sum_squares += i**2

for i in range(1,101):
    square_sum += i
square_sum = square_sum**2

print(square_sum)
print(sum_squares)
output = square_sum-sum_squares
print(output)