class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteriod in asteroids:
            while stack and stack[-1] > 0 and asteriod < 0:
                if stack[-1] < abs(asteriod):
                    stack.pop()
                elif stack[-1] == abs(asteriod):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteriod)

        return stack
