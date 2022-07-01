class Solution:
    def substitudeSpace(self, s):
        # res = ''
        # for str in s:
        #     if str == ' ':
        #         res = res + '%20'
        #     else:
        #         res = res + str
        # return res

        # counter = s.count(' ')
        # res = list(s)
        # res.extend([' '] * count * 2)
        # left, right = len(s) - 1, len(res) - 1
        # while left >= 0:
        #     if res[left] != ' ':
        #         res[right] = res[left]
        #         right -= 1
        #     else:
        #         res[right-2:right+1] = '%20'
        #         right -= 3
        #     left -= 1
        # return ''.join(res)

        # return '%20'.join(s.split(' '))

        n = len(s)
        for e, i in enumerate(s[::-1]):
            if i == ' ':
                s = s[:n-(e+1)] + '%20' + s[n-e:]
        return s

