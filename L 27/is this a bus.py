class vehicles:
    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

class Bus(vehicles):
    pass
School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:",School_bus.max_speed, "Mileage:", School_bus.milage)

