# Concatenate two lists index-wise
#           list1 = ["M", "na", "i", "Ke"]
#           list2 = ["y", "me", "s", "lly"]
#          Expected output: ['My', 'name', 'is', 'Kelly']

list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

# output:
# ['My', 'name', 'is', 'Kelly']