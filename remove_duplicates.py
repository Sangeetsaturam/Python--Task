# Remove duplicates items from the list of strings(Do the task with in built data types conversions)
#           list1 = ["Mike", "Emma", "Emma", "Kelly", "Mike", "Brad"]

def dup(x):
  return list(dict.fromkeys(x))

list = dup(["Mike", "Emma", "Emma", "Kelly", "Mike", "Brad"])
print(list)

# output:
#   ['Mike', 'Emma', 'Kelly', 'Brad']