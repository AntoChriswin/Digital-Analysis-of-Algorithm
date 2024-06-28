# Maximum Subarray
def maxSubArray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Length of Last Word
def lengthOfLastWord(s):
    words = s.split()
    return len(words[-1])

# Test the functions with examples
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Example 1:", maxSubArray(nums1))  # Output: 6

nums2 = [1]
print("Maximum Subarray Example 2:", maxSubArray(nums2))  # Output: 1

nums3 = [5, 4, -1, 7, 8]
print("Maximum Subarray Example 3:", maxSubArray(nums3))  # Output: 23

s1 = "Hello World"
print("Length of Last Word Example 1:", lengthOfLastWord(s1))  # Output: 5

s2 = "   fly me   to   the moon  "
print("Length of Last Word Example 2:", lengthOfLastWord(s2))  # Output: 4

s3 = "luffy is still joyboy"
print("Length of Last Word Example 3:", lengthOfLastWord(s3))  # Output: 6
