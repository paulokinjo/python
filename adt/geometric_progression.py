from progression import Progression
class GeometricProgression(Progression):
  
  def __init__(self, base = 2, start = 1):
    
    super().__init__(start)
    self._base = base
    
  def _advance(self):
    self._current *= self._base
    
print('Geometric progression with default base:')
GeometricProgression().print_progression(10)

print('Geometric progression with base 3:')
GeometricProgression(3).print_progression(10)