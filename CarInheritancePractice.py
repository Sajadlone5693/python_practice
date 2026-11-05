class Vehicle:
    def __init__(self,brand):
        self.brand=brand
        self.fuel=50
    def Drive(self):
        if self.fuel<10:
            print('lowfuel')
            return
        print('driving')
        self.fuel-=10
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model

    def honk(self):
        print('beep beep')

c=Car("toyota","new")
c.Drive()
c.Drive()
c.Drive()
c.Drive()
c.Drive()
c.Drive()
# c.Drive()

print(c.fuel)



