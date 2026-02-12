# Given a string of text, replace all occurrences of "&&" with "and" and all occurrences of "||" with
# "or". The "&&" and "||" will always have a space on either side of them.


import re

text = ""
pattern = ""

lines = int(input())

def repl(match):
    pattern = match.group(0)
    if "&&" in pattern:
        return str(pattern.replace("&&", "and"))
    if "||" in pattern:
        return str(pattern.replace("||", "or"))
    
if (lines < 100):
    for i in range(lines):
        text = text + input() + "\n"
else:
    print("Input exceeds limit of 100 lines.")

text = text.rstrip()

for t in text.splitlines():
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', repl, t))
