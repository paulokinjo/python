class Vector:
  """[Represent a vector in a multidimensional space.]  
  """
  
  def __init__(self, d):
    """[Create d-dimensional vector of zeros]    
    Args:
        d ([int]): [the vector dimension]        
    """
    self._coords = [0] * d
  
  def __len__(self):
    """[Return the dimension of the vector.]    
    """
    return len(self._coords)
    
  def __getitem__(self, j):
    """[Return jth coordinate of vector to given value]    
    Args:
        j ([int]): [coordinate of the vector]        
    """
    return self._coords[j]
  
  def __setitem__(self, j, val):
    """[Set jth coordinate of vector to given value]    
    Args:
        j ([int]): [coordinate of the vector]        
        val ([int]): [value to be set]
    """
    self._coords[j] = val
  
  def __add__(self, other):
    """[Return sum of two vectors]    
    Args:
        other ([Vector]): [Vector to be added with the Vector calling this method]
    """
    if len(self) != len(other):
      raise ValueError('dimensions must agree')

    result = Vector(len(self))
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    
    return result
  
  def __eq__(self, other):
    """[Return True if vector has same coordinates as other]

    Args:
        other ([Vector]): [The other vector to compare to]
    """
    return self._coords == other._coords
  
  def __ne__(self, other):
    """[Return True if vector differs from other]

    Args:
        other ([Vector]): [The other vector to compare to]
    """
    return not self == other
  
  def __str__(self):
    """[Produce string representation of vector]    
    """
    return '<' + str(self._coords)[1:-1] + '>'

v = Vector(5)           # construct five-dimensional <0, 0, 0, 0, 0>
print(v.__len__())
v[1] = 23               # <0, 23, 0, 0, 0>(based on use of _ _setitem_ _)
v[4] = 45              # <0, 23, 0, 0, 45>(also via _ _setitem_ _)
print(v[4])             # print 45 (via _ _getitem_ _)
u = v + v               # <0, 46, 0, 0, 90>(via _ _add_ _)
print(u)                # print <0, 46, 0, 0, 90>
print(v) 
total = 0
for entry in v:          # implicit iteration via _ _len_ _ and _ _getitem_ _
 total += entry
 
print(total)
 

v.__setitem__(2, 66)
print(v[2])
print(v == v)
print(v.__eq__(v))
print(v != v)
print(v.__ne__(v))

