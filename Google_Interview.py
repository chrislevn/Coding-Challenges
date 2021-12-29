"""
Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single character by a different character such that the resulting substring is a substring of t. In other words, find the number of substrings in s that differ from some substring in t by exactly one character.
For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', so this is a valid way.
Return the number of substrings that satisfy the condition above.
A substring is a contiguous sequence of characters within a string.
 
Example 1:
Input: s = "aba", t = "baba"
Output: 6
Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
The underlined portions are the substrings that are chosen from s and t.

​​Example 2:
Input: s = "ab", t = "bb"
Output: 3
Explanation: The following are the pairs of substrings from s and t that differ by 1 character:
("ab", "bb")
("ab", "bb")
("ab", "bb")
​​​​The underlined portions are the substrings that are chosen from s and t.

Example 3:
Input: s = "a", t = "a"
Output: 0

Example 4:
Input: s = "abe", t = "bbc"
Output: 10


"""

("aba", "baba")
"aba" "baa"

"aba"

"""

    b  a  b  a
a   
b 
a


"""


"""

dp = [[0 for i in range(len(letterOne))] for j in range(len(letterTwo))]

if letterOne[-1] != letterTwo[-1]: 
    dp[0][0] = 1
else: 
    dp[0][0] = 0

for i in range(len(letterOne)-1, -1, -1): 
    for j in range(len(letterTwo)-1, -1, -1): 
        if letter
        if  == 1: 
            dp[i][j] += 1
        else: 
            dp[i][j] = dp[i][j-1]

return dp[len(letterOne)-1][len(letterTwo)-1]


    b  a  b  a
a   
b 
a

S1: abade

S2: abbde

    a   b   a   d   e
a   0   1   1   2   2

b   

b

d

e


dp = [[0 for i in range(len(letterOne))] for j in range(len(letterTwo))]

for i in range(len(letterOne)): 
    for j in range(i+1, len(letterOne)): 
        if letterOne[i:j] != letterTwo[i:j]: 
            dp[i][j] = dp[i][j-1] + 1 
    
return dp[len(letterOne)-1][len(letterTwo)-1]

"""