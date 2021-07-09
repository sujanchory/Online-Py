class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        for i,j in dic.items():
            if j==1:
                return i
        
