class Solution:
    def twoSum(self, nums, target):
        # records = dict()
        # for idx, val in enumerate(nums):
        #     if target - val not in records:
        #         records[val] = idx
        #     else:
        #         return [records[target-val], idx]
        
        rec = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rec.get(rest, None) is not None:
                return [rec[rest], i]
            rec[nums[i]] = i