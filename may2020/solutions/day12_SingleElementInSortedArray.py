# You are given a sorted array consisting of only integers where every element appears exactly twice,
# except for one element which appears exactly once. Find this single element that appears only once.

# Note: Your solution should run in O(log n) time and O(1) space.

# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2

# Input: [3,3,7,7,10,11,11]
# Output: 10

def singleNonDuplicate(nums):
    low = 0
    high = len(nums)-1
    while low<high:
        mid = (low+high)//2
        if mid%2 == 0:
            if nums[mid] == nums[mid+1]:
                low = mid+2
            elif nums[mid] == nums[mid-1]:
                high = mid-2
            else:
                return nums[mid]        # This is because the index of the single element is always even
        else:
            if nums[mid] == nums[mid+1]:
                high = mid-1
            elif nums[mid] == nums[mid-1]:
                low = mid+1
    return nums[low]

# Alternate Solution:
# def singleNonDuplicate(nums):
#     return 2*sum(set(nums)) - sum(nums)
