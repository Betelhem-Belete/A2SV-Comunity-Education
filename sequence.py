def count_less_or_equal(arr, x):
    count = 0
    for num in arr:
        if num <= x:
            count += 1
    return count


def find_x(arr, k):
    left = 1
    right = 10**9
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if count_less_or_equal(arr, mid) >= k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result if count_less_or_equal(arr, result) == k else -1


# Reading input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Finding x
x = find_x(arr, k)

# Printing the result
print(x)
