class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots = []
        start = 0
        end = 1
        for s,e in slots1:
            slots.append((s,start))
            slots.append((e,end))
            
        for s,e in slots2:
            slots.append((s,start))
            slots.append((e,end))
            
        slots.sort()
        print(slots)
        
        previous = slots[0][0]
        
        available = 0
        
        for i in range(len(slots)):
            slot = slots[i][0]
            if available == 2 and (slots[i][0] - prev) >= duration:
                return [prev, prev+duration]
            
            if slots[i][1] == start:
                available+=1
                
            if slots[i][1] == end:
                available -=1
                
            prev = slot
        return []
            
            
                
