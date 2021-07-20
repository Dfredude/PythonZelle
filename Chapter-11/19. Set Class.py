
class set:
    def __init__(self, elements:list) -> None:
        self.elements = elements

    def addElement(self, x): self.elements.append(x)

    def deleteElement(self, x):
        while x in self.elements == True:
            self.elements.remove(x)
    
    def member(self, x): return x in self.elements

    def intersection(self, set2):
        inters = []
        for element in set2.elements:
            if element in self.elements:
                inters.append(element)
        return set(inters)

    def union(self, set2):
        return set(set2.elements + self.subtract(set2).elements)

    def subtract(self, set2):
        notinelements = []
        for element in self.elements:
            if element not in set2:
                notinelements.append(element)
        return set(notinelements)
            
