# 两数相减
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1): # i = 0, 1, 2
            a = nums[i] # a=2, i=0
            for j in range(len(nums)-i-1): # max j = 2(i=0),1(i=1),0(i=2)
                b = nums[i+j+1]
                if ((a + b) == target):
                    return [i, i + j + 1]
        return []
# 上面为两个for循环的暴力解法；
# 哈希表
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = {}
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target-num], i]
            hashtable[nums[i]] = i
        return []



if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    test = Solution()
    test1 = Solution1()
    import time
    current_time = time.time()
    output = test.twoSum(nums=nums,target=target)
    end_time = time.time()
    current_time1 = time.time()
    output1 = test1.twoSum(nums=nums, target=target)
    end_time1 = time.time()
    print(output, (end_time - current_time)*10000000)
    print(output1, (end_time1 - current_time1)*10000000)