def linear_sum(S, n):
  if n == 0:
    return 0
  else:
    return linear_sum(S, n - 1) + S[n - 1]
  
l = [1, 2]
linear_sum(l, len(l))

1 - linear_sum([1, 2], 2)
2 - linear_sum([1, 2], 1) + 2
3 - linear_sum([1, 2], 0) + 1
4 - 0 + 1
5 - 1 + 2
6 - 3