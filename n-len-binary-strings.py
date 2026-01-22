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
    
        return result  # <-- Add this line


print(binarystrings(5))