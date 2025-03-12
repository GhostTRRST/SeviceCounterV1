#Variables for the name of the customer, make and model of the vehicle, and the mileage of the vehicle.
isShopping = False


def shop():
    if isShopping is True:
        name = input("Please state your name. : ")
        makeModel = input("Please state the make and model of your vehicle. : ")
        mileage = int(input("Please state the mileage of your vehicle. : "))

        services = input("""The services we give include :
Oil change and tire rotation :
                          
$79.99 for oil and filter change
$30.00 for standard tires
$45.00 for 4WD or truck tires
                         
Brake pads and front end alignment :
                        
$120.00 for the package

Broken glass repair :

$69.99 for a large window
 """)
        



enter = input("Welcome to The WACTC Garage! Do you require any services? : ")
if enter == "yes":
    isShopping = True
    shop()
elif enter == "no":
    print("Okay, goodbye then!")
