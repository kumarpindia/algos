# Find all possibilities of a string with '?' replaced by '0' or '1'
# Description: This script generates all possible strings by replacing each
# occurrence of '?' in the input string with either '0' or '1'. It uses
# a recursive helper function to explore all combinations and stores the
# results in a list.

# For example, given the input "1?10", the output will be ["1010", "1110"].

# Time Complexity: O(2^m) where m is the number of '?' in the string.
# Space Complexity: O(2^m) for storing the results.

# The main function 'find_all_possibilities' initializes the result list
# and calls the helper function. The helper function builds the strings
# recursively by checking each character in the input string.


def find_all_possibilities(s):
    
    result = []
    helper(0, "", s, result)

    return result


def helper(i, slate, s, result):
    if i >= len(s):
        result.append(slate)
    else:
        if s[i] == "?":
            helper(i+1, slate + "0", s, result)
            helper(i+1, slate + "1", s, result)
        else:
            helper(i+1, slate + str(s[i]), s, result)


print (find_all_possibilities("1?10"))
print (find_all_possibilities("1?0?"))
