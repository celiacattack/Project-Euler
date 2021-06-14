#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time
start_time = time.time()

import math
count = 20
output = 1

while output == 1:
    count = count+20
    for i in [19,18,17,16,15,14,13,12,11]:
        if count % i != 0:
            output = 1
            break
        else:
            output = count

print(count)
print("--- %s seconds ---" % (time.time() - start_time))
