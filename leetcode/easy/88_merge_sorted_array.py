class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1

        for i in range(len(nums1)-1, -1, -1):
            """
            if any of the pointers reaches negative, that means i need to compare the value to -Infinity
            """
            val1 = nums1[p1] if p1 >= 0 else float("-inf")
            val2 = nums2[p2] if p2 >= 0 else float("-inf")
            if val1 > val2:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1

        return nums1
