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
print(get_destination_index("Los Angeles, USA"))

# Function to get the location of a traveler
def get_traveler_location(traveler):
  traveler_destination = traveler[1]  # Get the traveler's destination
  traveler_destination_index = get_destination_index(traveler_destination)  # Get the index of the traveler's destination
  return traveler_destination_index  # Return the index

# Get and print the location of the test traveler
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

# Initialize an empty list for attractions
attractions = []
for destination in destinations: 
  attractions.append([])  # Add an empty list for each destination

# Print the attractions list
print(attractions)

# Function to add an attraction to a destination
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)  # Get the index of the destination
  except SyntaxError:  # If there's a syntax error (e.g., destination not in list), return
    return

  attractions_for_destination = attractions[destination_index].append(attraction)  # Add the attraction to the destination's list