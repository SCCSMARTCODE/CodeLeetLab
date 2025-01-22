class Solution:  
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:  
        stack = []  
        
        for asteroid in asteroids:  
            while True:  
                # Check if the current asteroid is positive and the stack has a negative one on top  
                if asteroid > 0 or not stack or stack[-1] < 0:  
                    stack.append(asteroid)  
                    break  
                # Check for collisions  
                if stack[-1] < 0:  # If the top of the stack is negative, no collision occurs  
                    stack.append(asteroid)  
                    break  
                if stack[-1] == -asteroid:  # Both asteroids are equal and will destroy each other  
                    stack.pop()  
                    break  
                if stack[-1] < -asteroid:  # Stack's top asteroid is smaller (negative)  
                    stack.pop()  # Remove the top asteroid from the stack  
                    continue  # Continue to check the next asteroid in stack  
                break  # Top of stack is larger (positive) than the current one, no collision  

        return stack  