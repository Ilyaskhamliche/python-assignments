def binarysearch(arr, low, high, K):
    if low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == K:
            return mid
        elif arr[mid] < K:
            return binarysearch(arr, mid + 1, high, K)
        else:
            return binarysearch(arr, low, mid - 1, K)
    else:
        return -1


def binarySearch(arr, N, K):
    return binarysearch(arr, 0, N - 1, K)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = len(arr)
K = 5
result = binarySearch(arr, N, K)
print(result) 
