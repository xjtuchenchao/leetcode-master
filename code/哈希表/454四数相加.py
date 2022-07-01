class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # hashmap = dict()
        # for n1 in nums1:
        #     for n2 in nums2:
        #         if n1 + n2 in hashmap:
        #             hashmap[n1+n2] += 1
        #         else:
        #             hashmap[n1+n2] = 1
        # count = 0
        # for n3 in nums3:
        #     for n4 in nums4:
        #         key = - n3 - n4
        #         if key in hashmap:
        #             count += hashmap[key]
        # return count
        
        from collections import defaultdict
        rec = defaultdict(lambda : 0)  # TODO:总结一下这里的用法
        count = 0
        for i in nums1:
            for j in nums2:
                rec[i+j] += 1
        for i in nums3:
            for j in nums4:
                count += rec.get(-(i+j), 0)
        return count
            