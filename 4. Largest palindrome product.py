
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#If output is 5 then go ahead

import math
def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    return s[offset:offset+amount]

output_list = []

def main():
    for i in range (100,1000):
        for r in range(100,1000):
            calc = i*r
            if len(str(calc)) == 5:
                if left(str(calc),2) == right(str(calc),1)+mid(str(calc),3,1):
                    output_list.append(calc)
                    print(str(i)+' * '+str(r))
            elif len(str(calc)) == 6:
                if left(str(calc),3) == right(str(calc),1)+mid(str(calc),4,1)+mid(str(calc),3,1):
                    print(str(i) + ' * ' + str(r))
                    output_list.append(calc)
    print(output_list)
    print(max(output_list))

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#askjdfhlkajsdhflkjh
