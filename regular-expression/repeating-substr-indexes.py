# Given a string S and a string k, find all the indexes of the occurrences of k in S. If there are no
# occurrences, return (-1, -1).

# Sample Input
# abcdeabc
# abc 

# Sample Output
# (0, 2)
# (5, 7)

# Explanation
# The string "abc" occurs twice in the string "abcdeabc". The first occurrence starts at index 0 and ends
# at index 2. The second occurrence starts at index 5 and ends at index 7. Hence, the output is (0, 2)
# and (5, 7). If there were no occurrences of "abc" in "abcdeabc", the output would have been (-1, -1).
# Note: The indexing starts from 0. 
# You can assume that the string S contains only lowercase English letters and the string k also
# contains only lowercase English letters.


import re 

S = input()
k = input()
truncated_length = 0
found = False

if len(S) < 100 and len(k) < len(S):
    for i in range(len(S)):
        m = re.search(k, S)
        if m and m.end() > 0:
            found = True
            t = (m.start() + truncated_length, m.end() + truncated_length - 1)
            print(t)
            S = S[m.start()+1:]
            truncated_length = truncated_length + m.start() + 1
    if not found:
        print((-1, -1))

