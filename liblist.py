list1=["Articles","Newspapers","Comics","Journels","Books","Dictionaries"]
print("The given list:",'\n',list1)

print("\nLength of the list:",len(list1))

print("\nRepetation:",'\n',list1*3)

list1.append("Manuals")
print("\nThe list after applying append operation : ",'\n',list1)

list2=("Manuscript","Periodicals")
list1.extend(list2)
print("\nThe list after applying expend operation : ",'\n',list1)

list1.insert(3,"Encyclopedia")
print("\nThe list after applying insert operation : ",'\n',list1)

list1.remove("Comics")
print("\nThe list after applying remove operation : ",'\n',list1)

list1.pop(4)
print("\nThe list after applying pop operation : ",'\n',list1)

print('\nIndexing:')
print(list1[3])
print(list1[-1])

print('\nSlicing:')
print(list1[:4])
print(list1[2:5])
print(list1[0:4:2])

print('\nnegative Indexing:')
print(list1[::-1])

