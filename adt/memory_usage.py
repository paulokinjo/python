import sys
data = []
current = -1;
for k in range(2000):
  
  a = len(data)
  b = sys.getsizeof(data)
  
  if(current != b):
    current = b    
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
  data.append(None)
  
