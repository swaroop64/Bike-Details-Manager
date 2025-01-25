#Implementing bike details using __init__

class Bike():
    def __init__ (self,bike_name,bike_model,bike_edition,bike_engine_capacity,bike_milage,bike_price):
        self.a = bike_name
        self.b = bike_model
        self.c = bike_edition
        self.d = bike_engine_capacity
        self.e = bike_milage
        self.f = bike_price
    def bike_data(self):
        print("Bike Name: ",self.a)
        print("Bike Model: ",self.b)
        print("Bike Edition: ",self.c)
        print("Engine Capacity: ",self.d,"cc")
        print("Milage: ",self.e,"kmpl")
        print("Price: Rs.",self.f)
        print(f"The {self.a} {self.b} {self.c} edition comes with a {self.d}cc engine at a milage of {self.e} km per liter with a price of Rs.{self.f}")
while True:
        name=input("Enter the name of the bike: ")
        model=input("Enter the model of the bike: ")
        edition=input("Enter the edition of the bike: ")
        engine_capacity=int(input("Enter the engine capacity in cc: "))
        milage=float(input("Enter the mileage per km: "))
        price=int(input("Enter the price of the bike: "))
        
    
        my_bike = Bike(name,model,edition,engine_capacity,milage,price)
        my_bike.bike_data()

