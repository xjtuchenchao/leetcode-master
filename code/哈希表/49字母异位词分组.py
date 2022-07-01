class Solution:
    def groupAnagrams(self, strs):
        # groups = []
        # res = []
        # for i in range(len(strs)):
        #     str = strs[i]
        #     record = [0] * 26
        #     for j in range(len(str)):
        #         record[ord(str[j]) - ord("a")] += 1
        #     if record not in groups:
        #         groups.append(record)
        #         res.append([str])
        #     else:
        #         index = groups.index(record)
        #         res[index].append(str)
        # return res
        
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())
