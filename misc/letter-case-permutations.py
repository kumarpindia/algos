# Given a string s, return an array of all possible strings we can create by changing the case of the
# letters in s. The order of the output does not matter.

# Example 1:
# Input: s = "a1z"
# Output: ["a1z", "a1Z", "A1z", "A1Z"]
# Explanation: We can change the case of the letters 'a' and 'z' to create the permutations shown above.
# Note that we cannot change the case of the digit '1', so it remains the same in all permutations.

def letter_case_permutations(s):
    
    result = []
    slate = ""
    
    helper(s, 0, slate, result)
    
    return result


def helper(s, i, slate, result):
    if i == len(s):
        result.append(slate)
    else:
        if s[i].isalpha():
            helper(s, i+1, slate + str(s[i].upper()), result)
            helper(s, i+1, slate + str(s[i].lower()), result)
        else:
            helper(s, i+1, slate + str(s[i]), result)

print(letter_case_permutations("a1z")) # Output: ["a1z", "a1Z", "A1z", "A1Z"]
print(letter_case_permutations("G")) # Output: ["G", "g"]