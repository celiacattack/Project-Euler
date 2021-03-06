#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

max_value = 4000000

fib_1= 1
fib_2 = 2
total = 0

def even_check(x):
    global total
    if x % 2 == 0:
        total = total + x
        return total

def new_fibonacci(x,y):
    global fib_1
    global fib_2
    fib_1 = x
    fib_2 = y
    if fib_1 > fib_2:
        fib_2 += fib_1
        return fib_2
    else:
        fib_1 += fib_2
        return fib_1

def main():
    even_check(fib_1)
    even_check(fib_2)
    while fib_1 <= max_value or fib_2 <= max_value:
        print(fib_1,',',fib_2)
        new_fibonacci(fib_1,fib_2)
        even_check(fib_1)
        new_fibonacci(fib_1,fib_2)
        even_check(fib_2)
    print(total)

if 'main' == 'main':
    main()