class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        left_pointer = 0
        right_pointer = n - 1

        # find min index
        while left_pointer < right_pointer:
            middle = (left_pointer + right_pointer) // 2

            if nums[middle] > nums[right_pointer]:
                left_pointer = middle + 1
            else:
                right_pointer = middle

        min_index = left_pointer

        # normal case 
        if min_index == 0:
            left = 0
            right = n - 1
        # target value in first part of array
        elif target >= nums[0] and target <= nums[min_index - 1]:
            left = 0
            right = min_index - 1
        # target value in second part of array
        else:
            left = min_index
            right = n - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return -1

# Time complexity: O(log n)
# Space complexity: O(1)
