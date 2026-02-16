#Find common elements between two lists
list=[1,2,3,4,5]
list1=[1,6,7,8,5]

lst=set(list)
lst1=set(list1)

common_element=lst&lst1
print(F"the common element is :{common_element}")