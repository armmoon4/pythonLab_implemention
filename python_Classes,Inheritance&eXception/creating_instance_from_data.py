cityName = ['Detroit', 'Ann Arbor' , 'Pittusburgh' , 'Mars' , 'New York']
populations = [680250 , 117070 , 304391 , 1683 , 8406000]
states = ['MI' , 'MI' , 'PA' , 'PA' , 'NY']
city_tuples = zip(cityName , populations , states)
#print(city_tuples)

#city_tuples = list(zip(cityName, populations, states))  #converting in list to see output
#print(city_tuples)

class City:
    def __int__(self , n , p , s):
        self.name = n
        self.population = p
        self.state = s

    def __str__(self):
        return '{} , {} (pop: {})'.format(self.name , self.state , self.population)
cities = []
for city_tup in city_tuples:
    print(city_tup)
