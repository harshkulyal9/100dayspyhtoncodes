#Write a program to find the 1’s complement of a binary number and print it.
num = int(input("Enter the binary number: "))
place = 1
result = 0
valid = True

while num != 0:
    last_digit = num % 10

    if last_digit == 0:
        comp = 1
    elif last_digit == 1:
        comp = 0
    else:
        print("Invalid binary number")
        valid = False
        break

    result = result + comp * place
    place = place * 10
    num = num // 10

if valid:
    print("The 1's complement is:", result)
