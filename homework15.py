class Building:



    def __init__(self,numberOfFloors,buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType


    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFlors and self.buildingType == other.buildingType


b1 = (10, 'кирпич')
b2 = (10, 'кирпич')
print(b1 == b2)
b1 = (10, 'дерево')
b2 = (10, 'кирпич')
print(b1 == b2)
b1 = (15, 'дерево')
b2 = (10, 'кирпич')
print(b1 == b2)




