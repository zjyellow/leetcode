class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = {}
        for s in strs:
            str = "".join(sorted(s))
            if str in table:
                table[str].append(s)
            else:
                table[str] = [s]
        return table
if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    a = Solution()
    b = a.groupAnagrams(strs)
    print(b)