import time
from tqdm import tqdm
import math

user_input = int(input("Let's generate some prime numbers. How many you want, bitch?: "))

prime_list = [1]
number = 1

while len(prime_list) < user_input:
    for num in range(1,number): # testing prime for each number
        prime_list.append(number)
        if number == 1:
            prime_list.append(number)
        elif number % (num-1) == 0:
            del output_list[-1]

print(len(prime_list))    
