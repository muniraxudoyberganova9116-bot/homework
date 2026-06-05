# ## Generalized `Vector` Class  

# **Objective**: Create a Python class `Vector` that represents a mathematical vector in an n-dimensional space, capable of handling any number of dimensions.

# ### **Task Description**

# 1. **Create a `Vector` class** that represents a vector in an n-dimensional space.  
#    - The class should support vectors of any number of dimensions, defined by an arbitrary number of components provided during initialization.

class Vector:
    def __init__(self, *components):
        self.components = components
    
    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same number of dimensions")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])
    
    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("vectors must have the same number of dimensions")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __dot__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same number of dimensions")
        return sum(a *b for a, b in zip(self.components, other.components))
    
    def __scalar_mul__(self, scalar):
        return Vector(*[scalar * a for a in self.components])

    def __magnitude__(self):
        return sum(a ** 2 for a in self.components) ** 0.5

    def __normalize__(self):
        magnitude = self.__magnitude__()
        if magnitude == 0:
            raise ValueError("Cannot normalize a zero vector")
        return self.__scalar_mul__(1/magnitude)


    

a = Vector(1, 2, 3)
b = Vector(4, 5, 6)
c = a + b
print(c) 

d = a - b
print(d)

e = a.__dot__(b)
print(e)

f = a.__scalar_mul__(2)
print(f)

g = a.__magnitude__()
print(g)
h = a.__normalize__()
print(h)