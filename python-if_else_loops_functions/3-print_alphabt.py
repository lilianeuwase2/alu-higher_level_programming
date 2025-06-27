#!/usr/bin/python3
for char_code in range(97, 123):
    if char_code == 101 or char_code == 113:
        continue
    print(chr(char_code), end='')
print()
