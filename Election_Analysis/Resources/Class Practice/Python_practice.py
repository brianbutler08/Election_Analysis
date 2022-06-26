#print("Hello World")

#counties = ["Arapahoe", "Denver", "Jefferson"]
#if counties[1] == "Denver":
    #print(counties[1])
#if counties[2] != "Jefferson":
    #print(counties[2])
#temperature = int(input("What is the temperature outside?"))
#if temperature > 80:
    #print("Turn on the AC.")
#else:
    #print("Open the windows.")
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Yup")
else:
    print("Nope")
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

x = 0
while x <= 5:
    print(x)
    x = x + 1

for county in counties:
    print(county)

counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county, voters in counties_dict.items():
    print(str(county) + " county has " + str(voters) + " registered voters.")

import datetime
now = datetime.datetime.now()
print("The time right now is ", now)
