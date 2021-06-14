#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

import time
from tqdm import tqdm
import math

user_input = int(input("Let's generate some prime numbers. How many you want, bitch?: "))
prime_list = []

if user_input ==1:
    prime_list = [2]
elif user_input ==2:
    prime_list = [2,3]
elif user_input ==3:
    prime_list = [2,3,5]
else:
    prime_list = [48611]
    num = 48613
    while len(prime_list) < user_input:
        prime_list.append(num)
        for i in range(2,int((num/2)+1),2):
            if num%i == 0:
                del prime_list[-1]
                num = num+2
                break
            if i == int((num / 2)):
                num = num+2
                    
print(prime_list)
print(max(prime_list)) #printing solution
