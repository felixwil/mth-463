from os import system
from sys import argv

success = 0
for i in range(100):
    success += not system(f'p ca-panic.py {argv[1]} {argv[2]}')

print(success/100)