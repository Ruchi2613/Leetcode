'''1189. Maximum Number of Balloons
Easy
Topics
conpanies icon
Companies
Hint
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.'''


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        from collections import Counter

        text = Counter(text)
        counter_balloon = Counter("balloon")
        ans = 0

        while True:

            valid = True

            for key, value in counter_balloon.items():
                counter_left = text[key]

                if counter_left < value:
                    valid = False
                    break
                else:
                    text[key] -= value
            
            if valid == True:
                ans += 1

            else:
                break

        return ans 


