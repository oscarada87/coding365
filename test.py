from enum import Enum
class PetType(Enum):
    Dog = 'dog'
    Cat = 'cat'
print(PetType.Dog.value)
