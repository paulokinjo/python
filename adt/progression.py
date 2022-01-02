class Progression:
  def __init__(self, start=0):
    self._current = start
    
  def _advance(self):
    self._current += 1
    
  def __next__(self):
    if self._current is None:
      raise StopIteration()
    else:
      answer = self._current
      self._advance()
      return answer
    
  def __iter__(self):
    return self
  
  def print_progression(self, n):
    print(' '.join(str(next(self)) for j in range(n)))
    
print('Default progression:')
Progression().print_progression(10)