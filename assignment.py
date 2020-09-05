for i in range (10):
    print ('''  
    ========================================================
    |__| | |__/ |__/ /  \ /__` |__| |    /  ` |__|  /\  |\ | 
    |  | | |  \ |  \ \__/ .__/ |  | |    \__, |  | /~~\ | \| 
    =========================================================
    ''' )

    Volume = input ("please choose 1 for 1 Room, 2 for 2 Rooms,3 for 3 Rooms, 4 for more than 3 Rooms ")
    print("you selected {}".format(Volume))
    Volume = int(Volume)
    VPrice = 10000 * Volume
    line = "The volume price is {} JPY".format(VPrice)
    print(line)

    Distance = input ("please choose 1 for Same City, 2 for Same Perfecture, 3 for Less than 100Km, 4 for more than 100 Km but less than 500Km, 5 for more than 500Km ")
    print("You selected {}".format(Distance))
    Distance = int(Distance)
    DPrice = 20000 * Distance
    statement = "The Distance price is {} JPY".format(DPrice)
    print(statement)

    Bicycle = input ("please choose y for yes and n for No ")
      if(Bicycle =='y'):
       wbprice = 10000
       print ("you have a bicycle")
       print ("{} jpy".format(wbprice))
    elif(Bicycle =='n'):
        wobprice = 0
        print ("you have no bicycle")
        print ("{} jpy".format(wobprice))
    else:
        print ("Either y or n are allowed")


    Total = VPrice + DPrice
    Final = "The total amount is {} JPY".format(Total)
    print(Final)