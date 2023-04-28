from project.lizard import Lizard
from project.mammal import Mammal

mammal = Mammal("Stella")
print(mammal.__class__.__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__name__)
print(lizard.name)
