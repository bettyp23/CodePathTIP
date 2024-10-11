#Write a function is_prime() that takes in a positive 
# integer n and returns True if it is a prime number 
# and False otherwise. A prime number is a number 
# greater than 1 that has no positive divisors other 
# than 1 and itself.

def is_prime(n):
    while (n > 0):
        if ((n % n == 0 ) & (n / 1 == n )):
            return True
        else:
            return False

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))