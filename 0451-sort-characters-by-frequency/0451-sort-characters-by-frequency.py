class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        new=""
        sorted_freq=dict(sorted(freq.items(),key=lambda item:item[1],reverse=True))
        for key,value in sorted_freq.items():
            new+= key*value
        return new

        

        
            
        