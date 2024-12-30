class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k=k%n

        r = 0
        l = n-1

        #rotate all array
        while r<l:
            nums[l] , nums[r] = nums[r] , nums[l]
            r += 1
            l -= 1
        
        #rotate frist k element of the array
        r = 0
        l = k-1

        while r<l:
            nums[l] , nums[r] = nums[r] , nums[l]
            r += 1
            l -= 1
        
        #orate other part of the array
        r = k
        l = n-1

        while r<l:
            nums[l] , nums[r] = nums[r] , nums[l]
            r += 1
            l -= 1

# Time commplexity: O(n)
# Space complexity: O(1)

        
        
