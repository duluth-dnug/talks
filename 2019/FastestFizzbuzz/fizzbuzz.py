#!/usr/bin/env python3

def main():
    for i in range(1, 1000000001):
        fizz = (i % 3 == 0);
        buzz = (i % 5 == 0);
        if fizz and buzz:
            print("Fizzbuzz!")
        elif fizz:
            print("Fizz")
        elif buzz:
            print("Buzz")
        else:
            print("{:010d}".format(i))

if __name__ == "__main__":
    main()
