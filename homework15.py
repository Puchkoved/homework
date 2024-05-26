class Building:



    def __init__(self,numberOfFloors,buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType


    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


b1 = Building(10, 'кирпич')
b2 = Building(10, 'кирпич')
print(b1 == b2)
b1 = Building(10, 'дерево')
b2 = Building(10, 'кирпич')
print(b1 == b2)
b1 = Building(15, 'кирпич')
b2 = Building(10, 'кирпич')
print(b1 == b2)




