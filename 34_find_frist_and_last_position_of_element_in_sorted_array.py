class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = self.binarySearchModifyed(nums, target,True)
        r = self.binarySearchModifyed(nums, target,False)

        return [l,r]



    def binarySearchModifyed(self, nums ,target ,leftBias):
        right = len(nums) - 1
        left = 0
        middle_index = -1

        while right >= left:
            middle = (right + left) //2
            if nums[middle] == target:
                middle_index = middle

                if leftBias:
                    right = middle  - 1
                else:
                    left = middle + 1
            
            elif nums[middle]>target:
                right = middle -1
            else:
                left = middle +1

        return middle_index
            
        
