# Find CSS Color Codes
# Description: This script reads multiple lines of input and extracts all CSS color codes
# (both 3-digit and 6-digit hex codes) from each line using regular expressions.

# For example, given the input:
# 3
# background-color: #ABC;
# color: #123456; border: 1px solid #FFF;
# The output will be:
# #ABC
# #123456
# #FFF

import re

lines = []

n = int(input())

lines = [input() for _ in range(n)]

for line in lines:
    matches = re.finditer(r".(#[a-f0-9]{6}|#[a-f0-9]{3})", line, re.IGNORECASE)
    
    for match in matches:
        print(match.group(1))