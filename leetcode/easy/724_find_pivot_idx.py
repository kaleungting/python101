class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)

        for i, x in enumerate(nums):
            right_sum -= x

            if left_sum == right_sum:
                return i

            left_sum += x

        return -1



'''

think of a balance where you put all of the weight on one side, in order to know if they are balance, you take the weight from one side 
and put it on the other side. 

remove weight from right side, check to see if right and left are equal, and then place the weight on the left side

keep doing that until it balances and returns index
if not, return -1 

'''