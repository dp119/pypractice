
import re

N = int(input())
emails = []
for i in range(N):
    emails.append(input())
# print(emails)
pattern = re.compile('(^[a-z]{0,6}[_]*[@hacker.com])')
print(sorted(filter(pattern.match, emails)))


# '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
