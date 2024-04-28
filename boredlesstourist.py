# List of destinations
destinations = [
  "Paris, France",
  "Shanghai, China", 
  "Los Angeles, USA",
  "São Paulo, Brazil",
  "Cairo, Egypt"
]

# Test traveler data
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# Function to get the index of a destination in the destinations list
def get_destination_index(destination):
  destination_index = destinations.index(destination)  # Find the index of the destination
  return destination_index  # Return the index

# Print the index of "Los Angeles, USA"
# print(get_destination_index("Los Angeles, USA"))

# Function to get the location of a traveler
def get_traveler_location(traveler):
  traveler_destination = traveler[1]  # Get the traveler's destination
  traveler_destination_index = get_destination_index(traveler_destination)  # Get the index of the traveler's destination
  return traveler_destination_index  # Return the index

# Get and print the location of the test traveler
test_destination_index = get_traveler_location(test_traveler)
# print(test_destination_index)

# Initialize an empty list for attractions
attractions = []
for destination in destinations: 
  attractions.append([])  # Add an empty list for each destination

# Function to add an attraction to a destination
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)  # Get the index of the destination
  except SyntaxError:  # If there's a syntax error (e.g., destination not in list), return
    return

  attractions_for_destination = attractions[destination_index].append(attraction)  # Add the attraction to the destination's list

# Adding attractions for various cities with their associated tags
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])  # Adding an art museum in Shanghai
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])  # Adding a skyscraper in Shanghai
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])  # Adding an art museum in Los Angeles
add_attraction("Paris, France", ["Arc de Triomphe", ["monument", "historical site"]])  # Adding a historical monument in Paris
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])  # Adding a zoo in São Paulo
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])  # Adding a historical site in São Paulo
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])  # Adding a historical monument in Cairo
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])  # Adding a museum in Cairo

print(attractions)  # Printing the list of attractions

# Function to find attractions in a given city that match the user's interests
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)  # Getting the index of the destination in the list
  attractions_in_city = attractions[destination_index]  # Getting the attractions in the city


# Function to find attractions in a given city that match the user's interests
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)  # Getting the index of the destination in the list
  attractions_in_city = attractions[destination_index]  # Getting the attractions in the city
  attractions_with_interest = []  # Initializing an empty list for attractions with the user's interests
  for attraction in attractions_in_city:
    possible_attraction = attraction  # Get the attraction
    attraction_tags = attraction[1]  # Get the attraction's tags
    for interest in interests:  # For each interest
      if interest in attraction_tags:  # If the interest is in the attraction's tags
        attractions_with_interest.append(possible_attraction[0])  # Add the attraction to the list of attractions with the user's interests
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ['art'])  # Find art attractions in Los Angeles
print(la_arts) 

# function to connect people withj the attractions that they are interested in
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)

  interest_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
  for i in range(len(traveler_attractions)):
    if traveler_attractions[-1] == traveler_attractions[i]:
      interest_string += traveler_attractions[i] + "."
    else:
      interest_string += traveler_attractions[i] + ", "
  interest_string = interest_string.rstrip(", ")  # Remove the trailing comma and space
  return interest_string


smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
