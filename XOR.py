# Maximum Xor Problem
# Use the idea of Trie
def decimalToBinary(n):
    return bin(n).replace("0b", "")


def maxXor(arr, queries):
    n = len(bin(max(arr) + max(queries))) - 2
    bArr = [decimalToBinary(x).zfill(n) for x in arr]
    trie = makeTrie(bArr)
    ans = []

    for query in queries:
        bQuery = decimalToBinary(query).zfill(n)
        maxQ = ""
        current_trie = trie
        for c in bQuery:
            ch = c
            if str(int(ch) ^ 1) in current_trie:
                ch = str(int(ch) ^ 1)
            maxQ += ch
            current_trie = current_trie[ch]
        ans.append(int(maxQ, 2) ^ query)
    return ans


# Create a Trie from a list of numbers in binary representation
def makeTrie(binaryNumberList):
    trie = dict()
    for num in binaryNumberList:
        current_trie = trie
        for c in num:
            current_trie = current_trie.setdefault(c, {})
    return trie


def main():
    arr = [0, 1, 2]
    queries = [3, 7, 2]
    print(maxXor(arr, queries))


main()