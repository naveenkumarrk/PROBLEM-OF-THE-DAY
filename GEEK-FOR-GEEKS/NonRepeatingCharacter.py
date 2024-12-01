class Solution:
    def nonRepeatingChar(self,s):
      mp = {}
      for i in s:
          mp[i] = mp.get(i, 0) + 1
      for i, j in mp.items():
          if j ==1:
              return i
      return '$'

