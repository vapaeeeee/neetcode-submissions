class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += f"{len(string)}#{string}"
        return result

    #"5#Hello5#World11#like12#word"
    def decode(self, s: str) -> List[str]:
        pointer = 0
        result: List[str] = [] 
        while pointer < len(s):
            lastChar = False
            length = ""
            while lastChar != "#":
                if s[pointer] == "#":
                    lastChar = "#"
                    pointer += 1
                    break
                length += s[pointer]
                pointer += 1
            length_int = int(length)
            final_pos = pointer + length_int
            string = s[pointer:final_pos]
            result.append(string)
            pointer = final_pos
        return result