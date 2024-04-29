'''
-----TYPE 1 to write class-----
class Car:
    brand = None
    model = None

# print(Car.brand)
# print(Car.model)

Car.model = "TOYOTA"
print(Car.model)
'''

class Car:
    # class variables
    # brand = "yolo"
    total_cars = 0

    def __init__(self,brand,model):
        self.__brand = brand 
        self.__model = model
        Car.total_cars += 1

    def full_name(self):
        return f"Model:- {self.__model} and Brand:- {self.__brand}"
    
    def get_brand(self): #getter method to get the value of private variable
        return self.__brand
    
    def fuel_type(self):
        return "PETROL/DIESEL"
    
    @staticmethod # helps to give result even if self keyword is not given
    def general_description():
        return "this is the general description of the car"
    
    @property # helps to get the value of private variable
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "ELECTRICITY"
    
class Battery:
    def battery_info():
        return "this is battery"
    
class Engine:
    def engine_info():
        return "this is engine"
    
class ElectricCar2(Battery,Engine,Car):
    pass



#------- QUESTIONS ---------------

# question 1
myCar1 = Car("Toyata","Harrier") 
# print(myCar1.brand)
# print(myCar1.model)

myCar2 = Car("MG","ASTOR")
# print(myCar2.brand)
# print(myCar2.model)
# print(Car.brand) #possible only when it is a variable in class.

# question 2
# print(myCar1.full_name())
# print(myCar2.full_name())

# question 3
my_elec_Car1 = ElectricCar("Tesla","Series A","100kWH")
# print(my_elec_Car1.brand)
# print(my_elec_Car1.model)
# print(my_elec_Car1.full_name())
# print(my_elec_Car1.battery_size)

# question 4
# print(myCar2.brand)
# print(myCar1.get_brand())

# question 5
# print(myCar1.fuel_type())
# print(my_elec_Car1.fuel_type())

# doesn't work when self keyword is used
# print(Car.fuel_type())
# print(ElectricCar.fuel_type())

# question 6
# print(Car.total_cars)

# question 7
# print(Car.general_description())
# print(myCar1.general_description())
# print(myCar2.general_description())
# print(my_elec_Car1.general_description())

# question 8
# print(myCar1.get_brand())
# print(myCar1.model)
# myCar1.model = "INNOVA" #model value cannot be changed further. it is read-only
# print(myCar1.model)

# question 9
# print(isinstance(myCar1,Car))
# print(isinstance(myCar1,ElectricCar))
# print(isinstance(myCar2,ElectricCar))
# print(isinstance(my_elec_Car1,Car))
# print(isinstance(my_elec_Car1,ElectricCar))

# question 10
print(ElectricCar2.engine_info())
print(ElectricCar2.battery_info())