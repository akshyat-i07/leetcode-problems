class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}

        for i,j in zip(s,t):
            if i in dict1:
                if dict1[i]!=j:
                    return False
            if j in dict2:
                if dict2[j]!=i:
                    return False
            else:
                dict1[i]=j
                dict2[j]=i
        return True
        
            





        