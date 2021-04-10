# Max Array Sum Problem on HackerRank
def maxSubsetSum(arr):
    if len(arr) <= 2:
        return max(max(arr), 0)
    ans = [max(arr[0], 0), max(max(arr[0], arr[1]), 0)]
    for i in range(2, len(arr)):
        if arr[i] < 0:
            ans.append(ans[-1])
        else:
            ans.append(max(arr[i] + ans[-2], ans[-1]))
    return ans[-1]


def main():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print( maxSubsetSum(arr))


main()