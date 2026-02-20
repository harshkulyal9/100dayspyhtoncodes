# Lambda function to return (max, min)
min_max = lambda lst: (max(lst), min(lst))

lst = []   # Changed from () to []
n = int(input("Enter the length of list: "))

for i in range(n):
    value = int(input())
    lst.append(value)

result = min_max(lst)
print(f"The max and minimum value is: {result}")