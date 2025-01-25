class Vehical:
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage
    
modelX = Vehical(240, 18)

print("Model Max Speed:",modelX.max_speed)
print("Model Milage:", modelX.milage)