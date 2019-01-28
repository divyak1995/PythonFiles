from math import floor, ceil
from heapq import heappush, heappop

def RoundPrices(prices, target):
    heap = []
    result = [None] * len(prices)
    #floor every price
    for i in range(len(prices)):
        res[i] = floor(prices[i])
        heappush(heap, (-abs(res[i]-prices[i]), i))

    #To meet the target, we have to ceil prices of count target-sum(res)
    iteration = target - sum(res)

    while iteration > 0:
        #minimize the error by popping the highest value.
        value, index = heappop(heap) 
        res[index] = ceil(prices[index])
        iteration -= 1
        
    return res
    
prices=[30.3, 2.4, 3.5]
target=36
print RoundPrices(prices,target)
