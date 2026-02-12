# Given a string, find all the indices of the repeating vowels in it. If there are no repeating vowels,
# print -1.

# Sample Input
# escape special characters 
# Sample Output
# (1, 3)
# (3, 4)
# (5, 7)
# (7, 8)
# (9, 11)
# (11, 12)

# Explanation
# The string "escape special characters" has 6 pairs of repeating vowels. The first pair is "a" at
# indices 1 and 3. The second pair is "e" at indices 3 and 4. The third pair is "a" at indices 5 and 7.
# The fourth pair is "e" at indices 7 and 8. The fifth pair is "a" at indices 9 and 11. The sixth pair
# is "e" at indices 11 and 12. Hence, the output is (1, 3), (3, 4), (5, 7), (7, 8), (9, 11) and (11, 12).
# If there were no repeating vowels in the string, the output would have been -1.
# Note: The indexing starts from 0. You can assume that the string contains only lowercase English
# letters and spaces. You can also assume that the length of the string is less than 100.

str = "escape special characters"
vowels = "aeiouAEIOU"
prev = ""
result = ""
atleast_once = False

for char in str:
    if char and prev and char in vowels and prev in vowels:
        if result:
            result = result + char
        else:
            result = result + prev + char
        prev = char
        continue
    if result:
        print(result)
        result = ""
        atleast_once = True
    
    prev = char

if not atleast_once:
    print("-1")
        