# Email Validation
# Description: This script reads a number of email addresses from user input,
# validates them using a regular expression, and prints the valid email addresses
# in a formatted manner.
# The script uses the 'email.utils' module to parse and format email addresses.
# The regular expression used for validation checks for a valid username,
# an '@' symbol, a valid domain name, and a top-level domain of 1 to 3 letters.
# The script ensures that only valid email addresses are printed.

import re
import email.utils

eml = ""
emails = []

email_counts = int(input())

if email_counts < 100:
# can be rewritten as: emails = [email.utils.parseaddr(input()) for _ in range(email_counts)]
    for i in range(email_counts):
        eml = email.utils.parseaddr(input())
        emails.append(eml)

# can be rewritten as: for name, addr in emails:
for eml in emails:
    if re.search(r"^[a-zA-Z]+[\w.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$", eml[1]):
        print(email.utils.formataddr(eml))
