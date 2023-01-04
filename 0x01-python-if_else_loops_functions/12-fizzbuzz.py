#!/usr/bin/python3
def fizzbuzz():
    chr = []
    for i in range(1, 101):
        chr.append(i)

    for i in range(0, len(chr)):
        if chr[i] % 3 == 0 and chr[i] % 5 == 0:
            chr[i] = "FizzBuzz"
        elif chr[i] % 3 == 0:
            chr[i] = "Fizz"
        elif chr[i] % 5 == 0:
            chr[i] = "Buzz"

    for i in chr:
        print(i, end=" ")
