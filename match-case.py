# switch case

def day_of_week(day):
    match day:
        case 1:
            return "monday"
        case 2:    
            return "tusday"
        case 3:
            return "wednesday"
        case 4:    
            return "thursday"
        case 5:
            return "friday"
        case 6:    
            return "saturday"
        # 7 or 0
        case 7 | 0:    
            return "sunday"

number = int(input("input number "))
print(day_of_week(number))            