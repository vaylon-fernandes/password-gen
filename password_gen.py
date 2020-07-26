import secrets
from string import ascii_letters,digits,punctuation

temp = ascii_letters + digits + punctuation

length = int(input())

password = ''

for i in range(length):
	password = password + secrets.choice(temp)

print(password)