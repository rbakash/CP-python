class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("//", "/")
        if path[-1] == "/":
            path = path[:-1]
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
        # print("/" + "/".join(stack))
        return "/" + "/".join(stack)
