
# 1. Sliding Window Technique

arr = [2, 1, 5, 1, 3, 2, 4, 6]
k = 3

def max_subarray_sum(arr, k):
    max_sum = float("-inf")
    window_sum = 0
    left = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        if right >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[left]
            left += 1

    return max_sum

print(max_subarray_sum(arr, k))

# 2. Two Pointers Technique

def has_pair_with_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return False

target = 8
print(has_pair_with_sum(arr, target))