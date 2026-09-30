class Solution:

    def encode(self, strs: List[str]) -> str:
        l=[]
        for s in strs:
            l.append(str(len(s))+"#"+s)
        return "".join(l)


    def decode(self, s: str) -> List[str]:
        l1=[]
        i=0
        while i<len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+length+1]
            l1.append(word)
            i=length+j+1
        return l1

