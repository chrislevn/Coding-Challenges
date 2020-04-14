def Solution(s):
    length = len(s)
    for x in range(1,length):
        if (length % x == 0):
            lis =[s[y:y+x] for y in range(0,length,x) ]   # for x in range(0,length,y): ;  lis.append(exmp[x:x+y])
            lis_len = len(lis)
            for z in range(0,lis_len-1):
                if (lis[z] == lis[z+1]):
                    if (z==lis_len-2):
                        return lis_len

# #s= "abcabcabcabc"
# #s= "jaishreeramjaishreeramjaishreeram"
# #s= "harekrishnaharekrishnaharekrishnaharekrishna"
# exmp = "abcabcabcabc"
# print(solution(exmp))

s_1 = "abcabcabcabc"
s_2 = "abccbaabccba"
s_3 = "abcabcabcabc"
s_4 = "abccbaabccba"


def solution(string):
    res = 1
    for i in range(len(string)):
        length = int(len(string) / (i+1))
        flag = True
        for j in range(len(string)):
            if string[j] != string[j % length]:
                flag = False
                break
        if flag:
            res += 1
    return res

# def solution(s):
#     best = 1
#     # lets try from len(subarray) n to 1
#     for i in range(len(s)):
#         length = int(len(s) / (i + 1))
#         succ = True
#         for j in range(len(s)):
#             if s[j] != s[j % length]:
#                 succ = False
#                 break
#
#         if succ:
#             best = i + 1
#
#     return best

# def solution(s):
#     n = len(s)
#     if n<1:
#         return 0
#     # two pointers
#     p1 = 0
#     p2 = n-1
#     seq1, seq2 = '', ''
#     while p1<p2:
#         seq1 = seq1+s[p1]
#         seq2 = s[p2]+seq2
#         if seq1 == seq2 and seq1 == s[p1+1:p1+len(seq1)+1]:
#             return int(n/len(seq1))
#         p1+=1
#         p2-=1
#     return 1

                # checkList = [string[j:j+i] for j in range(0, len(string), i)]
                # lenCheck = len(checkList)
                # for j in range(0, lenCheck - 1):
                #     if checkList[j] == checkList[j+1]:
                #         if j == lenCheck - 2:
                #             return lenCheck


                # count = 1
                # start, end = 0, i
                # while i < len(string):
                #     # print(string[start:end])
                #     newStart = start + int(len(string) / i)
                #     newEnd = end + int(len(string) / i)
                #     print(string[start:end])
                #     print(string[newStart:newEnd])
                #     if string[start:end] == string[newStart:newEnd]:
                #         count += 1
                #     else:
                #         break
                #
                #     start += int(len(string) / i)
                #     end += int(len(string) / i)
                # res.append(count)


print(solution(s_1))
print(solution(s_2))
print(solution(s_3))
print(solution(s_4))
print(solution('abcabcN'))
print()

print(solution('a'))
print(solution('aa'))
print(solution('abcabc'))
print(solution('abcabcabc'))
print(solution('aaT'))
print(solution('ababT'))

print()
print(Solution(s_1))
print(Solution(s_2))
print(Solution(s_3))
print(Solution(s_4))

print(Solution('a'))
print(Solution('aa'))
print(Solution('abcabc'))
print(Solution('abcabcabc'))
print(Solution('aaT'))
print(Solution('ababT'))