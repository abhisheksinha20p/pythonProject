def is_leap(jj1):
    leap = True

    # Write your logic here
    if jj1 % 4 != 0:
        leap = False
    else:
        if jj1 % 100 != 0:
            leap = False

    return leap


year = int(input())
print(is_leap(year))
