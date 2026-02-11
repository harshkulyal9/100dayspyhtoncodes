''' Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
a) Fruits which are in both sets s1 and s2
b) Fruits only in s1 but not in s2
c) Count of all fruits from s1 and s2'''

set1 = {"apple", "banana", "mango", "orange"}
set2 = {"banana", "orange", "grapes"}

fruit_in_both=set1&set2
print(f"fruits in both s1 and s2 are:{fruit_in_both}")

fruit_only_set1=set1-set2
print(f"fruit only in s1 are:{fruit_only_set1}")

total_fruits=set1|set2
print(f"total fruits are :{len(total_fruits)}")

symmetric_difference=set2-set1|set1-set2
print(f"the symmetric difference is:{symmetric_difference}")