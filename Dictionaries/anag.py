#https://leetcode.com/problems/group-anagrams/submissions/
class Solution:

    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def create_dict1(self,s):
            d={}
            for i in s:
                if i not in d:
                    d[i]=0
                else:
                    d[i]+=1
            return d
        vis = [False]*len(strs)
        
        l=[]
        dict_l=[]
        for s in strs:
            dict_l.append(create_dict1(self,s))
        
        for i in range(len(strs)):
            if vis[i]:
                continue
            
            vis[i]=True
            d=dict_l[i]
            temp_l=[]
            temp_l.append(strs[i])
            #l.append()
            for j in range(i+1,len(strs)):
                if vis[j]:
                    continue
                if dict_l[j]==d:
                    temp_l.append(strs[j])
                    vis[j]=True
            l.append(temp_l)
        return l

            
