class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.split("/")
        stack = []

        for index, eachPath in enumerate(path):

            if eachPath == "..":
                if stack:
                    stack.pop()
            elif eachPath == "." or eachPath == "":
                continue
            else:
                stack.append(eachPath)

        return "/" + "/".join(stack)
