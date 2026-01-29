# The function computes a raised to b mod 10 raised to 9 + 7 efficiently 
# using the Binary Exponentiation (Exponentiation by Squaring) technique.
# This approach reduces the time complexity from O(b) (naïve multiplication) 
# to O(log b), making it suitable for very large exponents.

def calculate_power(a, b):
    mod = 1000000007
    result = 1
    
    if b == 0 or b > 1000000000 or a > 10000:
        return 1
    
    base = a % mod

    while b > 0:
        if b % 2 == 1:
            result = result * base % mod
        base = base * base % mod
        b //= 2
        
    return result
    
print(calculate_power(1, 1))
print(calculate_power(10000, 0))
print(calculate_power(123, 123))
print(calculate_power(10000, 1000000000))
print(calculate_power(100, 1000000000))
print(calculate_power(2, 10))
print(calculate_power(10000, 999999999))
print(calculate_power(3647, 851180738))
print(calculate_power(1406, 125968790))
print(calculate_power(1680, 166300905))
print(calculate_power(6930, 174080060))
print(calculate_power(3186, 151641717))