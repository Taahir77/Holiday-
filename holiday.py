

# dictionary "cost_city" gives a list of the travelling options and the price of each city

cost_city = {
    "Cape Town":1565,
    "Johannesburg":1150,
    "Durban":780,
    "Pretoria":925
    }

# defines the hotel cost with the number of nights as the argument
# the cost per night is R500 
# the total hotel cost is the cost per night multiplied by the number of nights
# the function then returns the total hotel cost

def hotel_cost(nights): 
    cost = 500 * int(nights)
    return cost

# defines the cost of the plane ticket with the city as the argument
# plane ticket costs are stored in the "cost_city" dictionary
# the function then returns the price of the plane ticket which determined by which city is selected

def plane_ticket(city):
    return cost_city[city]

# defines the cost of the rental car with the number of days as the argument
# car_days is the daily rate of renting the car multiplied by ther number of days the user wants to hire the car
# returns the total cost of hiring the car

def rental_car_cost(days): 

      car_days = 275 * days 
      return car_days
  
# defines the total cost of the holiday with 3 arguments: city, nights and car days 
# returns the total cost of the holiday which is caculated from the total_trip_cost variable in line 68
    
def total_holiday_cost(city, nights, car_days):
    total = hotel_cost(nights) + plane_ticket(city) +\
            rental_car_cost(car_days)
    return total

# city variable initiated to "none" until the user select a relevant city

city = None

#  while loop while this city variable holds true
# city variable then prompts the user to input a city
# if it is not a valid city, an error message is displayed on the screen
# if the entry is valid, the while loop then breaks and the code iterates to the next block of code

while True:
    city = input("Which city are you travelling to?\n")
    
    if city not in cost_city:
        print("That's not a valid destination.\n Please enter a valid destination")
    else:
        break

# hotel_nights is a variable that prompts the user to enter the amount of nights that they'll be staying at the hotel
# car_days variable prompts the user to enter the amount of days that they'll be hiring the car for

hotel_nights = input("\nHow many nights will you be staying?\n")
car_days = input("How many days will you hiring the car?\n")   

# total trip cost variable  calculates the final amount for the holiday which is accomodation, cost of the plane ticket and the cost of hiring a car
# the information gets sent to the def holiday_cost_function where the calculation is performed and the total is returned

total_trip_cost = hotel_cost(int(hotel_nights)) +\
                  plane_ticket(city) +\
                  rental_car_cost(int(car_days))


# displays to the user the total cost of the holiday

print("The total cost with the trip is", total_trip_cost)

















