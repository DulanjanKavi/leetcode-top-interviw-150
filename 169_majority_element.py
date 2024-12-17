class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        currentMajority=nums[0]
        noOfOverOther=1

        for i in range(1,n):
            if nums[i]==currentMajority:
                noOfOverOther+=1
            
            else:
                noOfOverOther-=1
                if noOfOverOther<0:
                    currentMajority=nums[i]
                    noOfOverOther=1
        
        return currentMajority

#Time complexity:O(n)
#Space complexity:O(1)
