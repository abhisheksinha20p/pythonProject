from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())
    # n = int(input()) i= 0 for i in range(n): if n>0: print(i**2) else: print("Invalid Number")
    for i in range(0, n):
        if n > 0:
            # The list of non-negative integers
            print(i ** 2)
