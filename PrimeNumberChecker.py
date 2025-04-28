import math
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

print(1,is_prime(1))
print(2,is_prime(2))
print(3,is_prime(3))
print(4,is_prime(4))
print(5,is_prime(5))
print(6,is_prime(6))
print(7,is_prime(7))
print(8,is_prime(8))
print(9,is_prime(9))
print(10,is_prime(10))
print(11,is_prime(11))