class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        point1=m-1 #what position get to campare in nums1
        point2=n-1 #what position get to campare in nums2
        point3=m+n-1 #what position need to modify in nums1

        while point3>=0:
            #nums1 out of index
            if point1<0:
                nums1[point3]=nums2[point2]
                point2-=1

            #nums2 out of index
            elif point2<0:
                break

            #nums1 value > nums2 value
            elif nums1[point1]>nums2[point2]:
                nums1[point3]=nums1[point1]
                point1-=1
            
            #nums1 value <= nums2 value
            else:
                nums1[point3]=nums2[point2]
                point2-=1
            
            point3-=1

#Time complexity: O(m+n)
#Space complexity: O(1)
