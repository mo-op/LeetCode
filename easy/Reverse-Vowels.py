'''
Write a function that takes a string as input and reverse only the vowels of a string.
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', A, E, I, O, U]
        ori = list(s)
        j = 0
        rev = ori[::-1]
        
        cur_len = len(rev)
        while (j < cur_len):
            if rev[j] in vowels:
                j += 1
            else:
                del rev[j]
                cur_len -= 1
        j = 0

        for i in range(0, len(ori)):
            if  ori[i] in vowels:
                ori[i] = rev[j]
                j += 1
        
        return ''.join(ori)
