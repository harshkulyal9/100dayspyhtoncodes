#WAP to input a list of scores for N students in a list data type. Find the score of the runner-
#up and print the output
n=int(input("enter the number:"))
lst=[]

for i in range(n):
    value=int(input())
    lst.append(value)

unique_word=sorted(set(lst))

if len(unique_word)<2:
    print(f"no runner present")
else:
    runner_up=unique_word[-2]
    print(F"the runner is: {runner_up}")
