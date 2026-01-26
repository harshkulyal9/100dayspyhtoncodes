#Write a program to calculate library fine based on late days as follows: 
'''First 5 days late: ₹2/day 
Next 5 days late: ₹4/day 
Next 20 days days late: ₹6/day 
More than 30 days: Membership Cancelled.'''
days = int(input("Enter number of days late: "))

fine = 0

if days <= 5:
    fine = days * 2
elif days <= 10:
    fine = (5 * 2) + (days - 5) * 4
elif days <= 30:
    fine = (5 * 2) + (5 * 4) + (days - 10) * 6
else:
    print("Membership Cancelled")
    exit()

print("Library Fine: ₹", fine)
