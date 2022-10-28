import sys
import numpy as np

f1 = sys.argv[1]
raw = np.loadtxt(f1, dtype=str)
out = map(lambda e: int(e, 16), raw)
f2 = sys.argv[2]
np.savetxt(f2, out, fmt='%d')
#print 'read from '+f1+' and write to '+f2
