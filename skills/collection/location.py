from geopy.geocoders import Nominatim


loc = Nominatim(user_agent="GetLoc")

getLoc = loc.geocode("Gosainganj Lucknow")

print(getLoc.address)

print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)


def get_address():
    location = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode()