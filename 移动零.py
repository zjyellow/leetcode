# 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c = 0
        for i in range(len(nums)):
            if nums[i-c] == 0:
                nums[i-c:-1] = nums[i-c+1:]
                nums[-1] = 0
                c+=1
        return nums
# 双指针
class Solution1(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums

if __name__ == '__main__':
    nums = [1,0,0,1,0,0,1,1,1]
    s = Solution()
    s1 = Solution1()
    output = s.moveZeroes(nums)
    output1 = s.moveZeroes(nums)
    print(output)
    print(output1)