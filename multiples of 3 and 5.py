#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

n = 0
count = 0

#logic to say whether n is divisible by 3 or 5, if yes then print n
def check_logic():
    global count
    if n % 3 == 0 or n % 5 == 0:
        count = count + n 
        return count

ask_number = int(input('what number would you like to solve for?: '))
while n != ask_number:
    n = n+1
    check_logic()
print('The total of all values divisible by 3 and 5 is: '+str(count))

