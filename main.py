import random
# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))
    

# Universal hashing
# size in this case - 1000 (since the test input is small it could be even smaller)
def universalHashFunction(x, a, b, p, m):
    return ((a * x + b) % p) % m

def process_queries(queries):
    result = []
    
    # Universal hashing
    hashSize = 1000 # Size of the hashTable, in this case is 1000 because the test input is small
    hashTable = [[] for i in range(hashSize)] # hashTable = bucket
    p = 1000000007 # P - large prime number constant used for hashing
    a = random.randint(1, p - 1) # a - random number from 1 to p - 1
    b = random.randint(0, p - 1) # b - random number from 0 to p - 1
    
    for currentQuery in queries:
        currentNumber = currentQuery.number # Assigned to a variable for readability
        hashValue = universalHashFunction(currentQuery.number, a, b, p, hashSize) # Hash value of the current number
        if currentQuery.type == 'add':
            for item in hashTable[hashValue]:
                if item[0] == currentNumber:
                    item[1] = currentQuery.name
                    break
            else:
                hashTable[hashValue].append([currentNumber, currentQuery.name])
        elif currentQuery.type == 'del':
            for item in hashTable[hashValue]:
                if item[0] == currentNumber:
                    hashTable[hashValue].remove(item)
                    break
        else:
            for item in hashTable[hashValue]:
                if item[0] == currentNumber:
                    result.append(item[1])
                    break
            else:
                result.append('not found')
    return result
# Average time complexity of the methods: O(1), with worst case o(k), where k - number of elements in the bucket
if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

