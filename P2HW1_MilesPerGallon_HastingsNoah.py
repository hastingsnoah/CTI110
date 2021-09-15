#This project is to promt users to enter miles fdriven, gallons used, prce per galon, and then calculates the
#mpg, total gas price, and price per mile.
#09-15-2021
#CTI-110 P2HW1-Miles Per Gallon
#Hastings, Noah

#Ask User to enter miles driven
miles_driven=float(input("Enter miles driven: "))
#Ask user  enter gallons used
gallons_used=float(input("Enter gallons used: "))
#Ask user to input cost per gallon
cost_per_gallon=float(input("Enter price per gallon: "))
#Calculate MPG (miles driven/gallons used)
mpg=miles_driven/gallons_used
#Calculate total gas cost (multipy cost per gallon by gallons entered)
total=cost_per_gallon*gallons_used
format_total="{:.2f}".format(total)
#Calculate cost per mile
cost_per_mile=mpg/cost_per_gallon
format_cost_per_mile="{:.2f}".format(cost_per_mile)
#Display miles per gallon, toal gas cost, cost per mile
print(("Miles Per Gallon: "),mpg)
print(("Total Gas Cost: $"),format_total, sep="")
print (("Cost Per Mile: $"),format_cost_per_mile,sep="")
