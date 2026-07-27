class Solution:
    def isValid(self, s: str) -> bool:
        queue = deque()

        for char in s:
            if char == "(" or char == "{" or char == "[":
                queue.append(char)
                continue
            if not queue:
                return False
            last = queue.pop()
            if char == ")":
                if last != "(":
                    return False
                else:
                    continue
            elif char == "}":
                if last != "{":
                    return False
                else:
                    continue
            else:
                if last != "[":
                    return False
                else:
                    continue
        return len(queue) == 0

