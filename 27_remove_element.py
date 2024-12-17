class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        #start and end use to track array element using its position
        start=0
        end=len(nums)-1

        #get array lenth 
        n = len(nums) 

        #get number array items equal to the val
        noOfRemove=0
        for i in range(n):
            if nums[i]==val:
                noOfRemove+=1

        #swap array elements
        while start<end:
            while nums[start]!=val and end>start:
                start+=1
            while nums[end]==val and end>start:
                end-=1
            if start>end:
                break
                
            nums[start],nums[end]=nums[end],nums[start]
        
        return n-noOfRemove

#Time complexity: O(n)
#Space complexity: O(1)
