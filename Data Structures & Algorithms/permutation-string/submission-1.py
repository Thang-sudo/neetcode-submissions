class Solution:
    def num(self, char: str) -> int:
        return ord(char) - ord('a')

    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 = [0] * 26
        f2 = [0] * 26
        for i in range(len(s1)):
            f1[self.num(s1[i])] += 1
        print(f1)
    
        for j in range(len(s2)):
            f2[self.num(s2[j])] += 1
            # the substring must have the same length as s1
            # move the window up by 1 if the current substring has more character than s1
            # remove the first character in windows
            if j >= len(s1):
                f2[self.num(s2[j - len(s1)])] -= 1
            if f1 == f2:
                return True
        return False



            