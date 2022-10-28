import sys
from filecmp import cmp

import numpy as np

height = np.loadtxt(sys.argv[1], dtype=int)
sa = np.loadtxt(sys.argv[2], dtype=int)
t = list(np.loadtxt(sys.argv[3], dtype=int))
#THRES_NUM = 1023 #511
THRES_NUM = int(sys.argv[4])
THRES_LEN = 4
MAXSHARE = 0
MAXID = 0
found_num = 0

for THRES_LEN in range(500, 10, -1):
  if found_num > 100:
    break
  print('============================> len = ' + str(THRES_LEN) + ' <==============================')

  cnt = 0
  breaks = height >= THRES_LEN
  start = []
  end = []
  for i in range(1,len(breaks)):
    if breaks[i-1] == False and breaks[i] == True:
      start.append(i)
    else:
      if breaks[i-1] == True and breaks[i] == False:
        if i - start[-1] < THRES_NUM - 200:
          start.pop()
        else:
          cnt = cnt + 1
          end.append(i)

  #print cnt
  #print zip(start,end)
  #print 'finish processing interval detect, start searching pattern'

  for a,b in zip(start,end):
    sa_id = a - 1
    t_id = sa[sa_id]
    pattern = t[t_id:t_id+THRES_LEN]

    i = 0
    cnt = 0
    target = t[0:0+THRES_LEN]
    position = []
    while i+THRES_LEN < len(t):

      if cmp(t[i:i+THRES_LEN], pattern)==0:
        cnt = cnt + 1
        position.append(i)
        i = i + THRES_LEN - 1
      i = i + 1

    if cnt <= THRES_NUM+1 and cnt > THRES_NUM-20:
      print('pattern = ')
      print(map(lambda e: hex(e).split('x')[-1][:-1], pattern))
      print('total occur = ' + str(cnt))
      print('position = ')
      print(position)
      print('------------------------------------')
      found_num = found_num + 1

  print("=====================================================================================")

## i = 0
## while i + THRES - 1 < len(height):
##   i = i + 1
##   interval = height[i:i+THRES]
##   share = min(interval)
##   if share > MAXSHARE:
##     MAXSHARE = share
##     MAXID = i - 1
## 
## print MAXID
## t_id = sa[MAXID]
## 
## # validate
## start = t_id
## l = 70
## pattern = t[start:start+l]
## i = 0
## cnt = 0
## while i+l < len(t):
##   if cmp(t[i:i+l], pattern)==0:
##     cnt = cnt + 1
##     print i
##     i = i + l - 1
##   i = i + 1
## 
## print cnt

