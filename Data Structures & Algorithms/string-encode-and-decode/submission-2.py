'''
I think just for the encode function, we can just have the number
 of characters in a string and then have a delimiter like a 
 hashtag and then the actual string. 

Then for the decode part, I think we can just, until we come across 
a number and then a hashtag, we'll use the number to cut out a 
substring of the string and append it to our list, and then 
continue doing that. 
'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            temp = f"{len(s)}#{s}"
            res += temp

        return res
        
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            string = s[j + 1: j + 1 + length]
            res.append(string)
            i = j + 1 + length
        
        return res


