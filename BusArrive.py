while True:
    hours = 60
    
    hour_now = int(input("Hour Now: "))
    save_hour = hour_now
    
    minute_now = int(input("Minute Now: "))
    
    time_now = (hour_now * hours) + minute_now
    
    bus_arrive = int(input("\nBus Arrive Every (Minutes): "))
    
    compute_bus_arrive = bus_arrive
    compute_hour_bus = 0
    
    while True:
        if compute_bus_arrive >= 60:
            compute_bus_arrive = compute_bus_arrive - 60
            compute_hour_bus = compute_hour_bus + 1
        else:
            break
            
    day = 0
    while True:
        if compute_hour_bus >= 24:
            compute_hour_bus -= 24
            day += 1
        else:
            break
                
    if compute_hour_bus <= 9:
        compute_hour_bus = "0" + str(compute_hour_bus)
    if compute_bus_arrive <= 9:
        compute_bus_arrive = "0" + str(compute_bus_arrive)
        
    print("Total Time of Every Arrive", day, "day/s", f"{compute_hour_bus}:{compute_bus_arrive}")
    
    time_bus_arrive = bus_arrive - (time_now % bus_arrive)
    
    if bus_arrive == time_bus_arrive:
        time_bus_arrive = 0
        
    minute_arrive = time_bus_arrive + minute_now
    
    while True:
        if minute_arrive >= 60:
            minute_arrive = minute_arrive - 60
            hour_now = hour_now + 1
        else:
           break
     
    day = 0
    hour_read = hour_now
    while True:      
        if hour_read >= 24:
            hour_read -= 24
            day += 1
        else:
            break
    
    if hour_read <= 9:
        hour_read = "0" + str(hour_read)
    if minute_arrive <= 9:
       minute_arrive = "0" + str(minute_arrive)
        
    print("\nBus Arrive in", day, "day/s", f"{hour_read}:{minute_arrive}")
    
    remain_hour = int(hour_now) - save_hour
   
    calculate_hour = remain_hour * 60
   
    remain_minute = (calculate_hour + int(minute_arrive)) - minute_now
   
    remain_hour = 0
    while True:
        if remain_minute >= 60:
            remain_minute -= 60
            remain_hour += 1
        else:
            break
            
    day = 0
    while True:
        if remain_hour >= 24:
            remain_hour -= 24
            day += 1
        else:
            break

    if remain_hour <= 9:
        remain_hour = "0" + str(remain_hour)
    if remain_minute <= 9:
        remain_minute = "0" + str(remain_minute)
        
    print("Remaining Time to Wait", day, "day/s",f"{remain_hour}:{remain_minute} \n\n")
           
           