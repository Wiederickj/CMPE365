
"""
CMPE 365 Assignment 1 
@Author: Jackson Wiederick| 20062602
“I certify that this submission contains my own work, except as noted"
"""


import math
start = 1 #Startings Airport
end = 199  #Destination 

#method used to ulpoad file and gather flight data 


def loadData(filename, PassType):
    #set paramters for LoadData function

    d = open(filename, "r") #open and read the file
    global NumofAir #Records The Number of AirPorts 
    NumofAir = int(d.readline())
    global flightList #create a matrix list to store all data
    flightList =[[] for k in range(0,NumofAir)] #create invidiual aiport lists

    for x in d.readlines():
        FlightData = []

        for z in x.split(PassType): #loop used to build the list of flight Data
            if z != "\n":
                FlightData.append(int(z))
        flightList[FlightData[0]].append(FlightData)
        #add the next flight information to list, loop again 


    return 




#Upload the file needed to load network
file = "2019_Lab_2_flights_real_data.txt" #filename

loadData(file, "\t") #open file
print("File: " + file + " , " + str(NumofAir) + " Airports have been found")
print("\n")
print("Starting and ending locations can be changed in the start and end variables")

TakeoffLocation = int(start)      #define the start location
AirportDestination = int(end)     #define the final destination  

Pathway =[[] for x in range(0,NumofAir)] #array to hold the flight path taken 
TimeofArrival = [math.inf]*NumofAir #if specified path is unable to be computed, set arrival time to null 


network = []  #holds the airports to be checked
network.append(TakeoffLocation) #add start point to the network
TimeofArrival[TakeoffLocation]=0 #starting location has a time of 0 to get there





while len(network) >0: #loop that runs until network is empty
    currlocation = network[0] #pick the first airport in the network
    network.sort(key=lambda x: TimeofArrival[x])#sort the network to find the current best time
    network.remove(currlocation)#remove the airport from network 



    for flightnumber in flightList[currlocation]: #for everyflight number that leaves its current location
        ArrivalDestination = flightnumber[1] #calls the final destintion 
        TimeofFlight = flightnumber[2] #calls the start time of flight
        ArrivalTime = flightnumber[3] #calls the arrival time

        

        if  ArrivalTime < TimeofArrival[ArrivalDestination] and TimeofFlight > TimeofArrival[currlocation]:#Check if the flight has left; check if flightpath to see if it is benificial


            network.append(ArrivalDestination) #recheck to make sure correct path was taken, add to the network
            newPath = Pathway[currlocation].copy() #Most effective path is added
            newPath.append(flightnumber)
            Pathway[ArrivalDestination] = newPath
            TimeofArrival[ArrivalDestination] = ArrivalTime #update arrivaltime with most effetive path
         #End of Algorithim   
            

if TimeofArrival[ArrivalDestination] != math.inf: #print statments showing the best route for specified airports
    print("Optimal route from " + str(TakeoffLocation) + " to " + str(AirportDestination)+ ":")
    print("\n")
    for flightnumber in Pathway[AirportDestination]:
        departingAirport = flightnumber[0] #call the airport num it is departing from 
        ArrivalDestination = flightnumber[1] #call the flight desitination
        TimeofFlight = flightnumber[2] #call the length of the flight
        ArrivalTime = flightnumber[3] #call the time of arrival to destination 
        print("Fly from " + str(departingAirport) + " at " + str(TimeofFlight) + ", to " + str(ArrivalDestination) + " arriving at " + str(ArrivalTime))
        
            












            
            
            
            
            
            
