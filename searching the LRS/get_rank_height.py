import sys
import numpy as np

t = list(np.loadtxt(sys.argv[1], dtype=int))
t.append(0)
sa = np.loadtxt(sys.argv[2], dtype=int)
rank_file = sys.argv[3]
height_file = sys.argv[4]

rank = [int]*len(sa)
for i in range(len(sa)):
  rank[sa[i]] = i
np.savetxt(rank_file, rank, fmt='%d')

height = [0]*len(sa)
k = 0;
for i in range(len(sa)):
  if k > 0:
    k = k-1 
  j = sa[rank[i]-1]
  while t[i+k] == t[j+k] :
    k = k+1
  height[rank[i]] = k #以index为等级的后缀数组重复的子串长度
np.savetxt(height_file, height, fmt='%d')

