class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                # The last asteroid on the stack is smaller and equal to the incoming one
                # Then it should be destroyed
                # if top of stack and incoming asteroid have the same size, both destroyed
                # Else the incoming asteroid is destroyed
                if stack[-1] < abs(a):
                    stack.pop()
                elif stack[-1] == abs(a):
                    stack.pop()
                    a = 0
                    break
                else:
                    a = 0
                    break
            if a != 0:
                stack.append(a)
        return stack