#!/usr/bin/env python3

#a = 65
#b = 8921

a = 699
b = 124

# star 2
while a % 4 != 0:
    a = (a * 16807) % 2147483647
while b % 8 != 0:
    b = (b * 48271) % 2147483647

count = 0

#for i in range(40000000):  # star 1
for i in range(5000000):  # star 2
    if (a & 0xffff) == (b & 0xffff):
        count += 1

    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    
    # star 2
    while a % 4 != 0:
        a = (a * 16807) % 2147483647
    while b % 8 != 0:
        b = (b * 48271) % 2147483647

print(count)
