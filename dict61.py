d={"Operating system":"Windows 10",
   "Microprocessor":"Intel(R) Core(TM) i3",
   "System memory":"8 GB",
   "Graphic device":"Intel(R) UHD Graphics",
   "Memory slot":"8GB Samsung 2667MHz"}

print("The defined Dictionary: ",'\n',d)

print("\nThe length of the dictionary: ",len(d))

print("\nRetrieving the value of \"Operating system\": ",d["Operating system"])

print("\nReassigning the value of \"Operating system\": ")
d["Operating system"]="Windows 10 Home Single Language 64-bit"
print("The Dictionary elements after reasigning ",d)

print("\nMembership Operator:")
print("Audio" in d)
print("Audio" not in d)

d["Audio"]="Realtek High Definition Audio"
print("\nThe Updated Dictionary Elements: ")
print(d)

del d["Memory slot"]
print('\nThe Dictionary elements after deleting \"Memory slot\" key:')
print(d)
