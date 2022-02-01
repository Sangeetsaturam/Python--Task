# Given the array of strings A,
# you need to find the longest string S which is the prefix of ALL the strings in the array.

def LCP(X, Y):
 
    i = j = 0
    while i < len(X) and j < len(Y):
        if X[i] != Y[j]:
            break
        i = i + 1
        j = j + 1
 
    return X[:i]
 
 
# Function to find the longest common prefix (LCP) between a given set of strings
def findLCP(words):
 
    prefix = words[0]
    for s in words:
        prefix = LCP(prefix, s)
    return prefix
 
 
if __name__ == '__main__':
 
    words = ["abcdefgh","abcefgh"]
    print('The longest common prefix is', findLCP(words))

# output:
#     The longest common prefix is abc