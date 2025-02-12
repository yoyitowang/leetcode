class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for char in strs:
            ans += f"{len(char)}#{char}"
        
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):

            j = s.find("#", i)
            length = int(s[i:j])

            ans.append(s[j+1: j+length+1])
            i = j+length+1
        return ans