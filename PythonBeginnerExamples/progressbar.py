import time
import sys
i=1
for i in range(10):
    #print i
    time.sleep(1)
    sys.stdout.write("%d%%" % i)
    sys.stdout.flush()
