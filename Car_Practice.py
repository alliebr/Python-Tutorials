#!/usr/bin/env python
# coding: utf-8

# In[2]:


# here is a simple class that would be a program for a car
class Car():
	"""A basic model of the coding in a car."""
	
# we initialize using the __init__() method, make sure it has “self” first, then add the parameters
# we also assign the intake variables of make, model, and year to internal class variables
# since this is for a new car, we set the odometer reading to 0
	def __init__(self, make, model, year):
		self.make = make	
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def check_gas_tank(level):
		print("Your gas tank is " + level)
		
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can’t roll back an odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles
		


# Now you can make an instance using the Car() class and play with it
my_gas_car = Car('subaru', 'outback', 2013)
print(my_gas_car.get_descriptive_name())

my_gas_car.update_odometer(23500)
my_gas_car.read_odometer()


# In[ ]:





# In[ ]:





# In[ ]:




