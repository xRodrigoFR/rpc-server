from datetime import datetime
import time
import rpyc
import sys
import os

start = time.time() 

if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))
 
server = sys.argv[1]
vector_n = sys.argv[2]

vector = []
for i in range (int(vector_n)):
    vector.append(i)
 
conn = rpyc.connect(server,4200)

print(conn.root.vector_sum(vector))

end = time.time()

start_time = datetime.fromtimestamp(start)
end_time = datetime.fromtimestamp(end)

print(f"Start: {start_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}, End: {end_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")