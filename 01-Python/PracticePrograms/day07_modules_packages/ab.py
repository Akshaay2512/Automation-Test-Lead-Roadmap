# Importing class methods from file a and b
#approach 1:
import a
import b

obj1 = a.Animal()
obj1.display()

obj2 = b.Bird()
obj2.display()

print("==" * 20, "Approach 2 ", "==" * 20)

#approach 2:
from a import Animal
from b import Bird

obj1 = Animal()
obj1.display()

obj2 = Bird()
obj2.display()

