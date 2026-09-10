class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[[p,s] for p,s in zip(position,speed)]
        stack=[]
        
        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
#If a car behind would arrive later or at the same time as the car in front, it joins that fleet (collides into it).
#A fleet is a group of cars that eventually reach the target together because the car behind cannot overtake the car in front.
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)