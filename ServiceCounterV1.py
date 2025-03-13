import os, time
#Shopping bool
isShopping = False

#all integer variables, counting how many dents, windows, and the cost.
cost = 0
smallDent = 0
largeDent = 0
largeWind = 0
smallWind = 0
cNum = 0

#service variable so i can track what service was chose
service = ""

#entire shopping process
def shop():
    if isShopping is True:
        global cost
        os.system("clear")
        #Gets the customers name, make and model of the vehicle, and the mileage of the vehicle.
        date = input("Please input the current date : ")
        print()
        time.sleep(1)
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

        #services that are included along with their prices. The customer can choose what service by using letters and numbers
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
        global service, largeDent, smallDent, smallWind, largeWind

        if services == "1-a":
            cost = cost + 79.99
            service = "oil and filter change"
        elif services == "1-b":
            cost = cost + 30
            service = "standard tires"
        elif services == "1-c":
            cost = cost + 45
            service = "4WD or truck tires"
        elif services == "2-a":
            cost = cost + 120
            service = "brake pads and front end alignment package"
        elif services == "3-a":
            lWind = int(input("How many large windows do you need repaired?: "))
            largeWind = lWind * 69.99
            cost = cost + largeWind
            service = "large window repair"
        elif services == "3-b":
            sWind = int(input("How many small windows do you need repaired?: "))
            smallWind = sWind * 39.99
            cost = cost + smallWind
            service = "small window repair"
        elif services == "4-a":
            time.sleep(1)
            sDents = int(input("How many small dents would you like to remove? :"))
            smallDent = sDents * 5
            cost = cost + smallDent
            service = "small dent removal"
        elif services == "4-b":
            lDents = int(input("How many large dents would you like to remove? :")) 
            largeDent = lDents * 15
            cost = cost + largeDent
            service = "large dent removal"


        print(f"""

        Date: {date}
        Customer number: {cNum}      
        Name: {name}
        Vehicle make+model: {makeModel}
        Mileage: {mileage}

        service: {service}
        Total: {cost}



""")
        
        

        
        
        



enter = input("Welcome to The WACTC Garage! Do you require any services? : ")
if enter == "yes" or "Yes" or "y":
    isShopping = True
    cNum = cNum + 1
    time.sleep(1)
    shop()
elif enter == "no" or "No":
    print("Okay, goodbye then!")
