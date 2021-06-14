#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import time
from tqdm import tqdm
import math

number = 600851475143
number2 = round(math.sqrt(number)) #mathematically the answer has to be less than sqrt of number
print((number))
output_list = []

for num in tqdm(range(2,number2-1)): # for loop to test each number between 2 and number whether it is a prime
    if number % num ==0:
        output_list.append(num)
        for r in range(2,num-1): # testing prime for each number
            if num % r == 0:
                del output_list[-1]
                break
    else:
        pass

print(output_list)