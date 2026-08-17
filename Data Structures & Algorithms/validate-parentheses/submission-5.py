class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        def is_match(ch1, ch2):
            match_dict = {")": "(", "]": "[", "}": "{"}
            return match_dict[ch1] == ch2

        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            if ch == ")" or ch == "]" or ch == "}":
                if len(stack) == 0:
                    return False
                if not is_match(ch, stack.pop()):
                    return False
        return len(stack) == 0
