# Last Updated: 5/15/2026, 11:15:21 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #---# use stack for opt sol-----
        stack = []
        for asteroid in asteroids:
            while stack and asteroid<0 and stack[-1]>0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack
            
            
                        
            
        

        