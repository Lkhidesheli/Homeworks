# class Car:   
#     number_of_cars = 0
#     def __init__(self, brand: str, model: str, year: int):
#         self.brand = brand
#         self.model = model
#         self.year = year
        
#         Car.number_of_cars += 1

#     def age_of_car(self) -> int:
#         current_year = 2026
#         return current_year - self.year

#     def car_info(self):
#         print(f"ბრენდი: {self.brand}, მოდელი: {self.model}, წელი: {self.year}, ასაკი: {self.age_of_car()} წლის.")

#     @classmethod
#     def total_cars(cls):
#         return f"სულ შექმნილია {cls.number_of_cars} მანქანა."

# class ElectricCar(Car):
#     def __init__(self, brand: str, model: str, year: int, battery_life: int):
#         super().__init__(brand, model, year)
#         self.battery_life = battery_life

#     def battery_info(self):
#         print(f"ელემენტის ხანგრძლივობა შეადგენს {self.battery_life} საათს.")

# car1 = Car("Toyota", "Camry", 2018)
# car2 = Car("BMW", "M5", 2022)
# tesla = ElectricCar("Tesla", "Model S", 2024, 12)

# print("მანქანების ინფორმაცია")
# car1.car_info()
# tesla.car_info()
# print("\nელექტრო მანქანის სპეციფიკაცია")
# tesla.battery_info()
# print("\nსტატისტიკა")
# print(Car.total_cars())