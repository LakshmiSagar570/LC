class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] == nums[mid ^ 1]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


# Explanation:
# So for this we cannot use a counter, since our PS says that we have to complete in O(log n) time and O(1) space.
# Since, counter takes O(n) time, it is not an efficient way to use counter
# Let's use Binary Search, since array is sorted
# Magical part is we use XOR operator instead of an if-elif ladder.
# Here's the tracing
# The key observation:
# Before the single element, every pair starts at an even index.
# After the single element, this pairing pattern gets shifted.
#
# Instead of checking:
#   if mid is even: compare with mid + 1
#   else: compare with mid - 1
#
# We use the XOR trick:
#   mid ^ 1
#
# It automatically gives the paired index:
#   0 ^ 1 = 1, 1 ^ 1 = 0 -> these are pairs=> (0,1);(2,3);(4,5)
#   2 ^ 1 = 3, 3 ^ 1 = 2
#   4 ^ 1 = 5, 5 ^ 1 = 4
#
# i.e.,
#   Even index -> Next index
#   Odd index  -> Previous index
#
# If nums[mid] == nums[mid ^ 1]:
#   -> Pair is intact.
#   -> The single element lies on the right.
#
# Otherwise:
#   -> Pairing has broken.
#   -> The single element lies on the left (including mid).
#
# Binary Search continues until left == right,
# which is exactly the index of the unique element.