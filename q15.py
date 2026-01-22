#Write a program to input a character and check whether it is an uppercase alphabet, lowercase alphabet, digit, or special character.
n=(input("enter the alphabet:"))

if n>="a" and n<="z":
    print(f"lower case")
elif n>="A" and n<="Z":
    print(f"upper case")
elif n>="0" and n<="9":
    print(f"digit")
else:
    print(f"special symbols")