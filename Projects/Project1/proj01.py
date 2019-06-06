#############################################
#Project1
#Input in rods
#convert the rods values to:
#Meters,Feet,Miles,Furlongs, and Minutes to walk
#############################################


rods_str = (input("Input rods: "))
rods_float = float(rods_str) 
print("You input",rods_float,"rods.",'\n')
print("Conversions")
meter_float = round(rods_float*5.0292,3)
print("Meters:",meter_float)
feet_float = round(rods_float*5.0292/0.3048,3)
print("Feet:",feet_float)
miles_float = round(rods_float*5.0292/1609.34,3)
print("Miles:",miles_float)
furlong_float = round(rods_float/40,3)
print("Furlongs:",furlong_float)
miles_per_hour = 3.1
miles_per_min =  miles_per_hour/60
minutes_to_walk = round(rods_float*5.0292/1609.34/miles_per_min,3)
print("Minutes to walk",rods_float,"rods:",minutes_to_walk)
