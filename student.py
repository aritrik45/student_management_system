class Student:
    college="Midnapore College Autonomous "
    def __init__ (self,id,name,dep):
        self.id=id
        self.name=name
        self.dep=dep
    def dict(self):
        return{
            "id":self.id,
            "name":self.name,
            "dep":self.dep
        }    