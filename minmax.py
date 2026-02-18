def num(a):
    minimum = a[0]
    maximum = a[0]

    for value in a:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value

    return minimum, maximum


n = [1, 2, 3, 4, 5]
print(f"The min and max value is: {num(n)}")
