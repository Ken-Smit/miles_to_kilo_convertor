#Kenneth Smith 4/6/2024 4.2
#This program is intended to convert miles to kilometers

#Created a function to covert miles to kilometers
def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    return kilometers

#Called the function using try/except blocks
try:
    miles = float(input("Enter the distance in miles: "))
    kilometers = miles_to_kilometers(miles)
    print(f"{miles} miles is equivelant to {kilometers} kilometers.")

except ValueError:
    print("Enter the correct value.")

