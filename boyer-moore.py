#coding:utf-8
def boyer_moore(long,short):
    #这一步是找出当前short的最长后缀
    #即找出所有前缀集合和后缀集合然后将其求并集然后在并集中找到最长的缀
    max_prefix=len(max(list(\
        set([short[:i+1] for i in range(len(short)-1)])&\
            set([short[i+1:] for i in range(len(short)-1)])\
                ),key=lambda x:len(x))) \
                    if len(short)>1 else 0
    print(max_prefix)
    length=len(short)
    #j是short内的循环pointer, k是short序列在long序列中的起始点
    j,k=length-1,0
    match={value:ind for ind,value in enumerate(short)}
    while k+length<=len(long):
        print(k)
        while short[j]==long[k+j] and j>=0:
            j-=1
        #j<0代表整个short都被成功匹配了, 那么就说明有该子串
        if j<0:
            return True
        #此时j<length-1代表从后往前至少有一位有匹配上, 所以进入好后缀模式
        elif j<length-1:
        #这个min是确保最长后缀的长度不超过已经匹配上的长度
        #如果超过了只能用已经匹配上的长度当做当前的后缀长度
            k+=length-min(max_prefix,length-1-j)
        #此时进入坏后缀模式
        else:
            #如果long[i]在short中出现过, 则返回最后一次出现的位置
            #如果long[i]未在short中出现过, 则往后跳一位
            k+=j-match[long[k+j]] if long[k+j] in match.keys() else j+1
        #每循环一轮就将j重置
        j=length-1
    return False
print(boyer_moore('HERE IS A SIMPLE EXAMPLE','EXAMPLE'))
