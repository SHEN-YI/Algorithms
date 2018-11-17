#Leetcode 94
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root):
    res=[]

    def helper(node,res):
        if node!=None:
            if node.left:
                helper(node.left,res)
            res.append(node.val)

            if node.right:
                helper(node.right,res)

    helper(root,res)
    return res

def inorderTraversal(root):
    stack,cur,res=[root],root,[]
    while cur or stack:
        while cur:
            stack.append(cur)
            cur=cur.left
        cur=stack.pop()
        res.append(cur)

#Leetcode 84
def largestRectangleArea(heights):
    stack,max_area=[-1],0
    for i in range(len(heights)):
        while stack[-1]!=-1 and heights[stack[-1]]>=heights[i]:
            max_area=max(heights[stack.pop()]*(i-stack[-1]-1),max_area)
        stack.append(i)
    while stack[-1]!=-1:
        max_area=max(heights[stack.pop()]*(len(heights)-stack[-1]-1),max_area)
    return max_area

#Leetcode 312
def maxCoins(nums):
    grid,nums={},[1]+[n for n in nums if n]+[1]
    def helper(i,j):
        if i+1==j: return 0
        if (i,j) not in grid:
            grid[i,j]=max(helper(i,k)+nums[i]*nums[k]*nums[j]+helper(k,j) for k in range(i+1,j))
        return grid[i,j]
    return helper(0,len(nums)-1)

def maxCoins(nums):
    nums=[1]+[n for n in nums if n]+[1]
    length=len(nums)-2
    grid=[[0]*len(nums) for i in range(len(nums))]
    for j in range(1,length+1):
        for i in range(j,0,-1):
            for k in range(i,j+1):
                grid[i][j]=max(grid[i][j],nums[i-1]*nums[k]*nums[j+1]+grid[i][k-1]+grid[k+1][j])
    return grid[1][length]

#leetcode 139
def wordBreak(s, wordDict):
    memo=[None]*len(s)
    def helper(start):
        if start==len(s):
            return True
        if memo[start]!=None:
            return memo[start]
        for end in range(start+1,len(s)+1):
            if s[start:end] in wordDict and helper(end):
                memo[start]=True
                return memo[start]
        memo[start]=False
        print(memo)
        return memo[start]
    return helper(0)

#top 10% dp solution of 139
def wordBreak(s,wordDict):
    char_set,char=set(),set(s)
    #if there is a character that in s but not in wordDict, return False
    for w in wordDict:
        char_set.update(w)
    if len(char)!=len(char_set&char):
        return False

    length=len(s)
    memo=[None]*length+[True]
    for i in range(length-1,-1,-1):
        for j in range(i+1,length+1):
            if s[i:j] in wordDict and memo[j]!=False:
                memo[i]=True
                break
        memo[i]=True if memo[i] else False
    return memo[0]

#leetcode 253
import heapq
def minMeetingRoom(intervals):
    if not intervals:return 0
    heap=[]
    intervals.sort(key=lambda x:x.start)
    heapq.heappush(heap,intervals[0].end)
    for i in intervals[1:]:
        if i.start>=heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap,i.end)
    return len(heap)
    
#top 5% queue solution of 253
def minMeetingRoom(intervals):
    start_list,end_list=[],[]
    for i in intervals:
        start_list.append(i.start)
        end_list.append(i.end)
    start_list.sort()
    end_list.sort()
    length,room=len(intervals),0
    start_pointer=end_pointer=0
    for i in range(length):
        if start_list[start_pointer]>=end_list[end_pointer]:
            end_pointer+=1
        else:
            room+=1
        start_pointer+=1
    return room
