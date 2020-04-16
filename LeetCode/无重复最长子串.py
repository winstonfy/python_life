#__author__ = 'Winston'
#date: 2020/2/20

def lengthOfLongestSubstring(s):
        if s is None or len(s) == 0: return 0;
        form = 0
        to =1
        maxlength = 1
        while to<len(s):
            site = s[form:to].find(s[to])
            if site != -1:
                length = to-form
                if length > maxlength:
                    maxlength = length
                form = form+site+1
            to += 1
        if to-form > maxlength:
            maxlength = to-form
        return maxlength














if __name__ == "__main__":
    s = 'a'
    obj = lengthOfLongestSubstring(s)
    print(obj)