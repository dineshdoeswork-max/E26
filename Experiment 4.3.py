# 4.3 Safe Division Kiosk (Exception Handling (try-except ))

def safe_division():
    print("-------BANKING KIOSK : SPLIT BILL --------")
    
    try:
        total = float(input("Enter the total amount: "))
        people = float(input("Enter the no. of people : "))
        
        result = total / people
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    
    except ValueError:
        print("Error: Please enter valid numeric values!")
    
    else:
        print(f"Result: {result:.2f}")
    
    finally:
        print("Thank you for using Safe Division Kiosk!")

safe_division()