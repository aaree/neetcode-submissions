class Person:
    def __init__(self, lastName: str, age: int, married: bool):
        self.lastName = lastName
        self.age = age
        self.married = married

    def getLastName(self) -> str:
        return self.lastName

    def getAge(self) -> int:
        return self.age

    def isMarried(self) -> bool:
        return self.married

class PersonFilter():
    def apply(self, person: Person) -> bool:
        ...

class AdultFilter(PersonFilter):
    # Implement Adult filter
    def apply(self,person:Person):
        if person.getAge()>=18:
            return True
        else:
            return False

class SeniorFilter(PersonFilter):
    def apply(self,person:Person):
        if person.getAge()>=65:
            return True
        else:
            return False

class MarriedFilter(PersonFilter):
    def apply(self,person:Person):
        if person.isMarried()==True:
            return True
        else:
            return False

class PeopleCounter:
    def __init__(self):
        self.filter: PersonFilter = None

    def setFilter(self, filter: PersonFilter) -> None:
        self.filter = filter

    def count(self, people: List[Person]) -> int:
        cnt=0
        for person in people:
            if self.filter.apply(person):
                cnt+=1
        return cnt
    
