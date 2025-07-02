class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicc={}
        i=-1
        for number in nums:
            i+=1
            need = target-number
            if need in dicc:
                return [dicc[need], i]
            else: 
                dicc[number]=i