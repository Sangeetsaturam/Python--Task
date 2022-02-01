# Write a program (function!) that takes a list and returns a new list that contains all 
# the elements of the first list minus all the duplicates.

def duplicates(a):
    x = []
    for i in a:
        if i not in x:
            x.append(i)
    return x
b = [1,2,3,4,4,3,1]
print(b)
print(duplicates(b))


# output:
#     1, 2, 3, 4, 4, 3, 1]
# [1, 2, 3, 4]