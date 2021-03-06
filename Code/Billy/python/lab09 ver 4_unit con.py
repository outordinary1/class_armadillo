import time

welcome_msg = '\nWelcome to unit converter!' # prints one letter at time
i = 0
while i < len(welcome_msg):
    print(welcome_msg[i], end='', flush=True)
    time.sleep(0.05)
    i += 1

time.sleep(1)

conv_rate = {"ft": .3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": .9144, "in": .0254} # conv rate dictionary

while True: 
    # def get_float(message): # input validation example
    #     while True:
    #         value = input(message)
    #         try:
    #             value = float(value)
    #             return value
    #         except ValueError:
    #             print("Sorry! That is an INVALID entry!")

    # user_dist = get_float("\nPlease enter distance: ")
    
    user_dist = float(input("\n\nPlease enter distance: "))

    time.sleep(0.5)
        
    user_unit_orig = input("Please enter units to CONVERT (ft, mi, m, km, yd, in): ").lower() # user input
    does_unit_orig_exist = conv_rate.get(user_unit_orig, False) # input validation

    if does_unit_orig_exist: # math if unit exists
        distance_meters = user_dist * (conv_rate.get(f"{user_unit_orig}"))
    else: # error message if unit does not exist
        print(f"Sorry! Unit '{user_unit_orig}' is NOT applicable!\n")
        exit()

    time.sleep(0.5)

    user_unit_desired = input("Please enter units DESIRED (ft, mi, m, km, yd, in): ").lower()
    does_unit_desired_exist = conv_rate.get(user_unit_desired, False)

    if does_unit_desired_exist: # final math if units desired units valid
        distance_new = distance_meters / (conv_rate.get(f"{user_unit_desired}"))

        time.sleep(1)

        print(f"\n{user_dist} {user_unit_orig} equals {distance_new} {user_unit_desired}\n") # results
        time.sleep(1)

        question = input("Would you like to convert another value? (yes/no): ").lower() # input for continue or not
        if question != "yes":
            time.sleep(0.5)
            print("\nSee you later!\n")
            exit()
    else: #if desired units invalid
        print(f"Sorry! Unit '{user_unit_desired}' is NOT applicable!\n")
        exit()



'''
Lab 9: Unit Converter
This lab will involve writing a program that allows the user to convert a number between units.

Version 1
Ask the user for the number of feet, and print out the equivalent distance in meters. 
Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. 
Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m

Version 2
Allow the user to also enter the units. Then depending on the units, convert the distance into meters. 
The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m

Version 3
Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m

Version 4
Now we'll ask the user for the distance, the starting units, and the units to convert to.

You can think of the values for the conversions as elements in a matrix, where the rows will be the units you're converting from, and the columns will be the units you're converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).

    ft	         mi	          m	        km
ft	1		                  0.3048	
mi		        1	          1609.34	
m	1/0.3048    1/1609.34	  1	        1/1000
km			                  1000	    1
But instead of filling out that matrix, and checking for each pair of units (if from_units == 'mi' and to_units == 'km'), we can just convert any unit to meters, then convert the distance in meters to any other unit.

Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. So first convert from the input units to meters, then convert from meters to the output units.

Below is some sample input/output:

> what is the distance? 100
> what are the input units? ft
> what are the output units? mi
100 ft is 0.0189394 mi
'''