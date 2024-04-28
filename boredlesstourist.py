destinations = [
  "Paris, France",
  "Shanghai, China", 
  "Los Angeles, USA",
  "São Paulo, Brazil",
  "Cairo, Egypt"
]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

'''
When a traveler arrives at a destination, we want to know where they are! 
Since we use lists for all of our data — we are going to identify 
each location based on its index in our destinations list. But we need to retrieve that index first.
'''
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

print(get_destination_index("Los Angeles, USA"))
# print(get_destination_index("Paris France, USA"))

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)


attractions = []
for destination in destinations: 
  attractions.append([])

print(attractions)

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  try:
    destination_index = get_destination_index(destination)
  except SyntaxError:
    return

  attractions_for_destination = attractions[destination_index].append(attraction)


add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)


