#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    args = len(argv) - 1

    for i in range(1, args):
        sum += int(argv[i])

print(f"{sum}")
