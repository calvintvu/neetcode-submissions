class Solution:

    def encode(self, strs: List[str]) -> str:

        string = ""
        for s in strs:
            string += (str(len(s)) + "#" + s)
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)

        while i < n:

            # get length to look at
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res