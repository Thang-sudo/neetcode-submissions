class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set('aeiou')
        result = []
        for c in s:
            if c not in vowels:
                result.append(c)
        return "".join(result)
