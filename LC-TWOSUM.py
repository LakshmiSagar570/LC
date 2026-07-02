def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1   # Need bigger sum → move left pointer right
        else:
            right -= 1  # Need smaller sum → move right pointer left
    return []
print(two_sum_sorted([1,2,3,4,5,6,7,8,9], 10))