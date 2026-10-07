class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                # The last asteroid on the stack is smaller and equal to the incoming one
                # Then it should be destroyed
                # Else the incoming asteroid is destroyed
                if stack[-1] < abs(a):
                    stack.pop()
                elif stack[-1] == abs(a):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(a)
        return stack