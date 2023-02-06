lst=[]
n=int(input("\nEnter the number of elements in a list: "))
print("\n")
for i in range(0,n):
    ele=(input("Enter the value "))
    lst.append(ele)
print("\nThe created list with duplicate elements: ",lst)
s=set(lst)
print("\nThe set after removing duplicate elements: ",s)
