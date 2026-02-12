# You are given a list of phone numbers. You have to check whether the given phone numbers are valid or 
# not. A valid phone number has 10 digits and starts with 7, 8 or 9.

# Input Format
# The first line contains an integer N, the number of phone numbers.
# The next N lines contain a phone number each. #Constraints # 1 <= N
# <= 100 #Output Format# For every phone number, print "YES" if the phone number is valid. Otherwise, 
# print "NO". Do not print the quotes.

#Sample Input# 2 # 9587456281 # 1252478965 
#Sample Output# YES # NO
#Explanation# 9587456281 is a valid phone number because it has 10 digits and starts with 9.
# 1252478965 is not a valid phone number because it does not start with 7, 8 or 9.


import re 

count_of_numbers = int(input())
numbers = ""

for i in range(count_of_numbers):
    numbers += input() + "\n"

for num in numbers.splitlines():
    match = re.search(r"^(7|8|9){1}\d{9}$", num)
    if match:
        print("YES")
    else:
        print("NO")