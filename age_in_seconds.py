#  Kyloexe
#  This is a meme program that calculates the age of the user in seconds on every planet and some moons lmao, using elliptical orbital mechanics lmao

#LIBRARIES
import math

#CONSTANTS

GRAVITATIONAL_CONSTANT = 6.67E-11
format(GRAVITATIONAL_CONSTANT, '.15f')
ONE_ASRTONOMICAL_UNIT = 1.495978707e11 #meters
ONE_SOLAR_MASS = 1.98847e30 #kilograms
PI = math.pi
SECONDS_IN_ONE_EARTH_YEAR = 31557600 # One Earth year in seconds 


#FUCNTIONS
def age():
    name_of_planet = input("Please input the name of the planet you are on: ")
    users_age_on_earth = int(input("Please input your age: "))
    semi_major_axis = float(input("Please input the semi-major axis of the orbit your planet around the star (in Astronomical Units => AU) "))
    mass_of_star = float(input("Please input the mass of the star your planet is orbiting (in Solar Masses (1 Solar mass = ) "))
    
    
    
    distance_of_planet_from_star = (semi_major_axis * ONE_ASRTONOMICAL_UNIT)
    mass_of_users_star = (mass_of_star * ONE_SOLAR_MASS)
    mu = (GRAVITATIONAL_CONSTANT * mass_of_users_star) # Mu is the Standard Gravitational parameter, used is celestial mechanics
    
    orbital_period = ((2 * PI) * (math.sqrt(((distance_of_planet_from_star ** 3)/mu))) / SECONDS_IN_ONE_EARTH_YEAR) # This is Kepler's Third Law, aka the equation to find the orbital period of the users planet
    
    users_age_on_planet_earth_years = (users_age_on_earth * orbital_period)
    users_age_on_planet_planet_years = (users_age_on_earth / orbital_period)

    users_age_on_planet_earth_years_printed = print(f"The user is {users_age_on_planet_earth_years:.0f} years old on Earth.")
    users_age_on_planet_planet_years_printed = print(f"The user is {users_age_on_planet_planet_years:.0f} years old on {name_of_planet}.")
    print("~"*100)

    print("Thanks for using my program!")
    print("Here are some links to sources I used to get some of the constants and formulas: ")
    print("Kepler's Third Law => https://en.wikipedia.org/wiki/Orbital_mechanics#Elliptical_orbits")
    print("Gravitational constant => https://en.wikipedia.org/wiki/List_of_physical_constants (It's G)")
    
age()
