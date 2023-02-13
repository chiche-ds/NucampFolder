inches_snow = {
    "Monday":2,
    "Tuesday": 4,
    "Wednesday": 5
}

def total_inches(inches_snow):
    n = 0   #varibale to hold inches of snow 
    for inches in inches_snow.values():
        n += inches
    print("Total snowfall inches ", n )

total_inches(inches_snow)

sn = int(input("How many inches of snow fell on Thursday? "))
inches_snow.update({"Thursday": sn })  #sn to hold the input of thurday 

total_inches(inches_snow)