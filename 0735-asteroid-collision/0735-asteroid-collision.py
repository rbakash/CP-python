class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteriod in asteroids:
            flag = True
            while stack and stack[-1] > 0 and asteriod < 0:
                if stack[-1] < abs(asteriod):
                    stack.pop()
                elif stack[-1] == abs(asteriod):
                    flag = False
                    stack.pop()
                    break
                else:
                    flag = False
                    break
            if flag:
                stack.append(asteriod)

        return stack
