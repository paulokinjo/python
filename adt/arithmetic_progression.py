from progression import Progression

class ArithmeticProgression(Progression):
  
  def __init__(self, increment = 1, start = 0):
    
    super().__init__(start)
    self._increment = increment
    
  def _advance(self):
    self._current += self._increment
    
print('Arithmetic progression with increment 5:')
ArithmeticProgression(5, 2).print_progression(10)