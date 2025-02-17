class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        ting = s.split(" ")
        rtn = []
        for i in reversed(ting):
            if i == " " or i == "":
                continue
            rtn.append(i.strip())
        delim = " "
        return delim.join(rtn).strip()

