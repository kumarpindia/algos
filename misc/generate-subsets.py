# Given a string, generate all possible subsets of the characters in the string. 
# The order of the subsets does not matter.
# For example, given the string "xy", the subsets would be: "", "x", "y", "xy".

# The function uses a helper function to recursively build the subsets by 
# including or excluding each character. The main function initializes the 
# necessary variables and calls the helper function, which performs the actual 
# subset generation. The results are returned as a list of subsets.

# Example usage is provided at the end, where the function is called with the 
# string "xy" to generate its subsets.

# Time complexity: O(2^n) where n is the length of the input string, due to the 
# recursive nature of the subset generation.

def generate_all_subsets(s):
    
    slate = ""
    result = []
    arr = list(s)
    pshelper(slate, arr, result)

    return result
    

def pshelper(slate, arr, result):
    if len(arr) == 0:
        result.append(slate)
    else:
        pshelper(slate + arr[0], arr[1:], result)
        pshelper(slate, arr[1:], result)


print(generate_all_subsets({"s": "xy"}))
print(generate_all_subsets("xy"))