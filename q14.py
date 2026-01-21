#Write a program to input a character and check whether it is a vowel or consonant using if–else.
n=(input("enter the character:")).lower()

if n=="a" or n=="e" or n=="i" or n=="o" or n=="u":
    print(f"vowel")
else:
    print(f"consonant")