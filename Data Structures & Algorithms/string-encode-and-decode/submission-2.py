class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            num_digits = len(str(len(s)))
            out += str(num_digits) # Number of digits to read
            out += str(len(s)) # Length of string
            out += s # actual string
        # strings look like this:
        # 15Hello15World
        return out

    def decode(self, s: str) -> List[str]:
        results = []
        i = 0
        print(s)
        while i < len(s):
            # read the length of next word then the word and move to the next number
            digitNum = int(s[i])
            wordLength = int(s[i + 1 : i + digitNum + 1])
            start = i + 1 + digitNum 
            end = i + 1 + digitNum + wordLength 
            results.append(s[start : end])
            i = end
        return results