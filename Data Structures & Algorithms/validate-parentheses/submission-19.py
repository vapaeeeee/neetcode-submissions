class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        print("str: " + s)
        for i in range(len(s)):
            print("stack: ")
            print(stack)
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    opener = stack.pop()
                    print("opener: " + opener)
                    if opener == "(" and s[i] == ")":
                        continue
                    elif opener == "{" and s[i] == "}":
                        continue
                    elif opener == "[" and s[i] == "]":
                        continue
                    else:
                        return False
        return len(stack) == 0