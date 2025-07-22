class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Awali dengan string pertama
        prefix = strs[0]

        # Bandingkan dengan string lain satu per satu
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # potong satu karakter dari belakang
                if prefix == "":
                    return ""
        return prefix
