# Generate all binary strings of length n
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)

def binarystrings(n):
    if n == 1:
        return ["0", "1"]
    else:
        prev_result = binarystrings(n-1)
        result = []
        for s in prev_result:
            result.append(s + "0")
            result.append(s + "1")
    
        return result


print(binarystrings(5)) 
# Output: ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001',
# '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011', '10100',
# '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111']