'''3842. Toggle Light Bulbs
Easy
Topics
Hint
You are given an array bulbs of integers between 1 and 100.

There are 100 light bulbs numbered from 1 to 100. All of them are switched off initially.

For each element bulbs[i] in the array bulbs:

If the bulbs[i]th light bulb is currently off, switch it on.
Otherwise, switch it off.
Return the list of integers denoting the light bulbs that are on in the end, sorted in ascending order. If no bulb is on, return an empty list.

 

Example 1:

Input: bulbs = [10,30,20,10]

Output: [20,30]

Explanation:

The bulbs[0] = 10th light bulb is currently off. We switch it on.
The bulbs[1] = 30th light bulb is currently off. We switch it on.
The bulbs[2] = 20th light bulb is currently off. We switch it on.
The bulbs[3] = 10th light bulb is currently on. We switch it off.
In the end, the 20th and the 30th light bulbs are on.
Example 2:

Input: bulbs = [100,100]

Output: []

Explanation:

The bulbs[0] = 100th light bulb is currently off. We switch it on.
The bulbs[1] = 100th light bulb is currently on. We switch it off.
In the end, no light bulb is on.
 

Constraints:

1 <= bulbs.length <= 100
1 <= bulbs[i] <= 100
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
59,991/83.4K
Acceptance Rate
71.9%'''

class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        
        # solution 1:
        on_d = {}

        for b in bulbs:
            if b not in on_d:
                on_d[b] = 1
            elif b in on_d:
                del on_d[b]


        sortt = sorted(on_d.keys())

        return sortt
    
        # solution 2:
        on_d = {}

        for b in bulbs:
            if b not in on_d:
                on_d[b] = 1
            elif b in on_d:
                del on_d[b]

        res = []
        for b, freq in on_d.items():
            if freq %2 ==1:
                res.append(b)
        res.sort()
        return res