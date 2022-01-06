def reverse(S, start, stop):
  if start < stop - 1:
    S[start], S[stop-1] = S[stop - 1], S[start]
    reverse(S, start + 1, stop - 1)
    
l = list('paulo')
reverse(l, 0, len(l))
print(''.join(l))