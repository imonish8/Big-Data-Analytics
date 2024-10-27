import random

city_names = ['Paris', 'London', 'NewYork', 'New Jersey']

city_temps = {city: random.randint(20, 30) for city in city_names}

print(city_names)
print(city_temps)
