# Coding assignments for Array & String topic
def isUnique(st):
    arr = [0] * 255
    for i in range(len(st)):
        if arr[ord(st[i])] != 0:
            return False
        else:
            arr[ord(st[i])] = 1
    return True


def isPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    d = {}
    for i in range(len(s1)):
        if s1[i] not in d:
            d[s1[i]] = 1
        else:
            d[s1[i]] += 1
        if s2[i] not in d:
            d[s2[i]] = -1
        else:
            d[s2[i]] -= 1
    
    for v in d.values():
        if v != 0:
            return False
    return True


def isPermutation2(s1, s2):
    return sorted(s1) == sorted(s2)


def urlify(st, n):
    subst = st[:n]
    subst = subst.replace(" ", "%20")
    return subst


def isPermutationOfPalindrome(st):
    d = {}
    st = st.lower()
    for i in range(len(st)):
        if 'a' <= st[i] <= 'z':
            if st[i] not in d:
                d[st[i]] = 1
            else:
                d[st[i]] += 1

    count = 0
    for v in d.values():
        if v % 2 != 0:
            count += 1
    if count > 1:
        return False
    return True


def oneAway(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    i, j = 0, 0
    while i < len(s1) and j < len(s2) and s1[i] == s2[j]:
        i += 1
        j += 1
    if len(s1) == len(s2) and s1[i+1:] == s2[j+1:]:
        return True
    if i == len(s1) or s1[i:] == s2[j+1:]:
        return True
    return False


def printMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], " | ", end="")
        print()


# rotate matrix in-place
def rotateMatrix(mat):
    print("ORIGINAL MATRIX")
    printMatrix(mat)

    n = len(mat)
    for i in range(n):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for i in range(n):
        for j in range(n//2):
            mat[i][j], mat[i][n-1-j] = mat[i][n-1-j], mat[i][j]

    print("AFTER ROTATE 90 deg")
    printMatrix(mat)
    return mat


def main():
    # print(isUnique("Thien Y Tr"))
    # print(isPermutation("123456709", "901476532"))
    # print(urlify("Thien Y Tran      ", 12))
    # print(isPermutationOfPalindrome("Tact Coa"))
    # print(oneAway("pale", "bake"))
    rotateMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])


main()
