import unittest

#returns array with shortest distance from each char in S to the specific char C
def shortestToChar(S,C):
    index = []
    dist = []

    #go through S and find index of all C
    for i in range(len(S)):
        if S[i] == C:
            index.append(i)
    
    print(index)

    min_dist = float('inf')

    #go through S again and find the minimum distance to all values of index array
    for i in range(len(S)):
        for j in range(len(index)):
            min_dist = min(min_dist, abs(i - index[j]))
        
        dist.append(min_dist)
        min_dist = float('inf')
    
    return dist
    
#Still a work in progress...
def shortestToCharOptimized(S,C):
    index = [] #[3, 5, 6, 11]
    dist = []

    #go through S and find index of all C
    for i in range(len(S)):
        if S[i] == C:
            index.append(i)
    
    comp1, comp2 = None, None

    for i in range(len(S)):
        j, k = 0, len(index) - 1

        while j < len(index) and index[j] < i:
            j += 1

        while k > 0 and index[k] > i:
            k -= 1
        
        dist.append(min(abs(i - index[j]), abs(i - index[k])))
    
    return dist

class myTest(unittest.TestCase):
    def test(self):
        self.assertEqual(shortestToChar("loveleetcode", 'e'), [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])
        self.assertEqual(shortestToCharOptimized("loveleetcode", 'e'), [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])
        self.assertEqual(shortestToCharOptimized("aaba", 'b'), [2, 1, 0, 1])

unittest.main()