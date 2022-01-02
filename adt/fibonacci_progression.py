from progression import Progression

class FibonacciProgression(Progression):
  
  def __init__(self, first = 0, second = 1):
    
    super().__init__(first)
    self._prev = second - first
    
  def _advance(self):
    
    self._prev, self._current = self._current, self._prev + self._current
    
print('Fibonacci progression with default start values:')
FibonacciProgression().print_progression(10)

print('Fibonacci progression with start values 4 and 6')
FibonacciProgression(4, 6).print_progression(10)