#Write a program that accepts a percentage (0-100) and assigns a grade based on the following criteria: 
'''90-100: Grade A 
80-89: Grade B 
70-79: Grade C 
60-69: Grade D 
below 60: Grade F.'''

n=int(input("enter the number:"))

if n>=90 and n<=100:
    print(f"GRADE A")
elif n>=80 and n<=89:
    print(f"GRADE B")   
elif n>=70 and n<=79:
    print(f"GRADE C") 
elif n>=60 and n<=69:
    print(f"GRADE D")
elif n<60  and n>0:
    print(f"GRADE F")
else:
    print(f"invalid")
