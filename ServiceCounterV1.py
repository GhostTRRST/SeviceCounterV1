import os, time
# Variables for the name of the customer, make and model of the vehicle, and the mileage of the vehicle.
isShopping = False
cost = 0


def shop():
    if isShopping is True:
        global cost
        os.system("clear")
        name = input("Please state your name : ")
        print()
        time.sleep(1)
        makeModel = input("Please state the make and model of your vehicle : ")
        print()
        time.sleep(1)
        mileage = int(input("Please state the mileage of your vehicle : "))
        print()
        time.sleep(3)
        os.system("clear")

        services = input("""The services we give include :
                         
Oil change and tire rotation :
                          
$79.99 for oil and filter change
$30.00 for standard tires
$45.00 for 4WD or truck tires
                         
Brake pads and front end alignment :
                        
$120.00 for the package

Broken glass repair :

$69.99 for a large window
$39.99 for a small window

Dent removal : 
                    
$5.00 per small dent
$15.00 per large dent
 
Please type 1-4 to choose category and a-c for service (ex. 1-a) : """)

        if services == "1-a":
            cost = cost + 79.99
        elif services == "1-b":
            cost = cost + 30
        elif services == "1-c":
            cost = cost + 45
        



enter = input("Welcome to The WACTC Garage! Do you require any services? : ")
if enter == "yes":
    isShopping = True
    time.sleep(1)
    shop()
elif enter == "no":
    print("Okay, goodbye then!")
