# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base Class (Tier 1)
class Vehicle():
    pass

# Tier 2 Class
class GroundVehicle(Vehicle):
    pass

# Tier 3 Class
class Car(GroundVehicle):
    pass

# Tier 3 Class
class Motorcycle(GroundVehicle):
    pass

# Tier 2 Class
class FlightVehicle(Vehicle):
    pass

# Tier 3 class
class Airplane(FlightVehicle):
    pass

# Tier 3 class
class Starship(FlightVehicle):
    pass