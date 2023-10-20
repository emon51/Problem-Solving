class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for s in strs:
            res += ">" + s
        return res[1:]

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res = []
        curr = ""
        for i in range(len(str)):
            if str[i] == ">":
                res.append(curr)
                curr = ""
            else:
                curr += str[i]
        res.append(curr)
        return res

        
