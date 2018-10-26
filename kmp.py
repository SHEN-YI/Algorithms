def pmt(s):
    """
    建立部分匹配表
    """
    prefix = [s[:i+1] for i in range(len(s)-1)]
    postfix = [s[i+1:] for i in range(len(s)-1)]
    intersection = list(set(prefix) & set(postfix))
    if intersection:
        #找出最长的前缀和后缀
        return len(max(intersection,key=lambda x:len(x)))
    return 0
def kmp(big,small):
    '''
    big代表需要被匹配的长的字符串, small代表用来匹配的短的字符串
    '''
    i = 0
    while i < len(big) - len(small) + 1:
        #当i>len(big)-len(small)+1的时候剩下的需要匹配的字符串长度都不如small的长度长, 就没有必要接着试了
        match = True
        for j in range(len(small)):
            if big[i+j] != small[j]:
                match = False
                break
        if match:
            return True
        #移动位数 = 已匹配的字符数 – 对应的部分匹配值
        if j:
        #如果pmt(small[:j])的结果为0说明在当前已经匹配的字符中没有可供新一轮匹配开始的起始点, 那么就全部跳过已匹配的字符
        #注意此处是对于已匹配的字串计算其部分匹配表, 而不是一开始就对整个small进行计算, 如果对整个small计算的话就不是 部分 匹配表了
            i += j - pmt(small[:j])
        else:
            i += 1
    return False
print(kmp('ababcabcacbab','abcac'))
