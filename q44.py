#Write a program to find the sum of the series: 1 + 3/4 + 5/6 + 7/8 + … up to n terms.
n = int(input("Enter number of terms: "))
sum = 0

for i in range(1, n + 1):
    term = (2*i - 1) / (2*i)
    sum = sum + term

print("Sum of the series is:", sum)
