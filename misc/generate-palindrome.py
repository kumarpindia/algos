# This function generates all palindromic decompositions of a given string. 
# A palindromic decomposition is a way of breaking down a string into substrings 
# such that each substring is a palindrome. The function uses a helper function 
# to recursively build the decompositions and check for palindromic properties.

# The main function initializes the necessary variables and calls the helper 
# function, which performs the actual decomposition and palindrome checking. 
# The results are returned as a list of palindromic decompositions.
# Example usage is provided at the end, where the function is called with the 
# string "abracadabra" to generate its palindromic decompositions.

# Time complexity: O(n * 2^n) where n is the length of the input string, due to 
# the recursive nature of the decomposition and palindrome checking.

def generate_palindromic_decompositions(s):
    
    result = []
    slate = s[0]
    last_string = s[0]
    i = 1
    
    pdhelper(s, i, slate, last_string, result)
    
    return result
    
    
def pdhelper(s, i, slate, last_string, result):
    if i == len(s):
        if (last_string == last_string[::-1]):
            result.append(slate)
        return
    
    pdhelper(s, i+1, slate + s[i], last_string + s[i], result)
    
    if (last_string == last_string[::-1] and last_string):
        pdhelper(s, i+1, slate + "|" + s[i], s[i], result)


print(generate_palindromic_decompositions("abracadabra"))