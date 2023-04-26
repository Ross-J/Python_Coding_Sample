# Conversion Program for converting numerical values between base number systems

# 1st Pattern - commonly used base systems converted to base 10 (decimal)
def binaryToDecimal(value):
    answer = 0
    place = 1
    for i in range(len(value) - 1, -1, -1):
        answer = answer + (int(value[i]) * place)
        place = place * 2
    return answer
     
def binaryToDecimalAlternate(value):
    reversedValue = ""
    for c in value:
        reversedValue = c + reversedValue
    answer = 0 
    place = 1
    for c in reversedValue:
        if(c == '1'):
            answer = answer + place
        place = place * 2
    return answer
    
def octalToDecimal(value):
    answer = 0
    place = 1
    for i in range(len(value) - 1, -1, -1):
        answer = answer + (int(value[i]) * place)
        place = place * 8
    return answer
    
def decimalToDecimal(value):
    answer = 0
    place = 1
    for i in range(len(value) - 1, -1, -1):
        answer = answer + (int(value[i]) * place)
        place = place * 10
    return answer
    
def hexidecimalToDecimal(value):
    answer = 0
    place = 1
    hextets = "0123456789ABCDEF"
    for i in range(len(value) - 1, -1, -1):
        answer = answer + (hextets.find(value[i]) * place)
        place = place * 16
    return answer
    
def anyBaseToDecimal(value, radix): # up to base 36
    answer = 0
    place = 1
    possibleVals = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(value) - 1, -1, -1):
        answer = answer + (possibleVals.find(value[i]) * place)
        place = place * radix
    return answer
    
    
 

# 2nd Pattern - base 10 (decimal) converted to commonly used base systems
def decimalToBinary(value):
    answer = ""
    while(value > 0):
        remainder = value % 2
        value = value // 2
        answer = str(remainder) + answer
    return answer
    
def decimalToOctal(value):
    answer = ""
    while(value > 0):
        remainder = value % 8
        value = value // 8
        answer = str(remainder) + answer
    return answer
    
def decimalToHexidecimal(value):
    answer = ""
    hextets = "0123456789ABCDEF"
    while(value > 0):
        remainder = value % 16
        value = value // 16
        answer = hextets[remainder] + answer
    return answer
    
def decimalToAnyBase(value, radix):
    answer = ""
    hextets = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while(value > 0):
        remainder = value % radix
        value = value // radix
        answer = hextets[remainder] + answer
    return answer
    
    

# Change Calculation Program for calculating necessary change required for a transaction
# Takes in user input for monetary amounts paid and owed; returns detailed change results

def getAmountOwed():
    amountOwed = input("Please enter the total amount owed, in dollars and cents: $")
    for c in amountOwed:
        if(c != '0' and c != '1' and c != '2' and c != '3' and c != '4' and c != '5' and c != '6' and c != '7' 
        and c != '8' and c != '9' and c != '.'):
            print("Invalid input. Please re-enter amount, making sure format is correct")
            return False
    return amountOwed
            
def getAmountPaid():
    amountPaid = input("Please enter the total amount paid, in dollars and cents: $")
    for c in amountPaid:
        if(c != '0' and c != '1' and c != '2' and c != '3' and c != '4' and c != '5' and c != '6' and c != '7' 
        and c != '8' and c != '9' and c != '.'):
            print("Invalid input. Please re-enter amount, making sure format is correct")
            return False
    return amountPaid
    
def displayChange(totalChange, dollars, quarters, dimes, nickels, pennies):
    print(f"Your total change is ${round(totalChange, 2)}")
    if(dollars != 0):
        if(dollars == 1):
            print(f"{int(dollars)} dollar")
        else:
            print(f"{int(dollars)} dollars")
    if(quarters != 0):
        if(quarters == 1):
            print(f"{int(quarters)} quarter")
        else:
            print(f"{int(quarters)} quarters")
    if(dimes != 0):
        if(dimes == 1):
            print(f"{int(dimes)} dime")
        else:
            print(f"{int(dimes)} dimes")
    if(nickels != 0):
        if(nickels == 1):
            print(f"{int(nickels)} nickel")
        else:
            print(f"{int(nickels)} nickels")
    if(pennies != 0):
        if(pennies == 1):
            print(f"{int(pennies)} penny")
        else:
            print(f"{int(pennies)} pennies")
       
def calculateChange(amountOwed, amountPaid):
    totalChange = amountPaid - amountOwed
    changeLeft = totalChange
   
    dollars = changeLeft // 1 
    changeLeft = changeLeft % 1 
    
    quarters = changeLeft // 0.25
    changeLeft = changeLeft % 0.25
    
    dimes = changeLeft // 0.1 
    changeLeft = changeLeft % 0.1 
    
    nickels = changeLeft // 0.05
    changeLeft = changeLeft % 0.05
    
    pennies = changeLeft // 0.01
    changeLeft = changeLeft % 0.01
    
    displayChange(totalChange, dollars, quarters, dimes, nickels, pennies)
    
    
    
    



# Examples - calling functions with various parameters 
def main():
    print(binaryToDecimal("1010"))
    print(binaryToDecimalAlternate("1010"))
    print(anyBaseToDecimal("1010", 2))
    
    print(octalToDecimal("1375"))
    print(anyBaseToDecimal("1375", 8))
    
    print(decimalToDecimal("1998"))
    print(anyBaseToDecimal("1998", 10))
    
    print(hexidecimalToDecimal("BAD"))
    print(anyBaseToDecimal("BAD", 16))
    
    print(anyBaseToDecimal("15AGZ", 36))



    amO = getAmountOwed()
    while(amO == False):
        amO = getAmountOwed()
    amP = getAmountPaid()
    while(amP == False):
        amP = getAmountPaid()
    
    amountOwed = round(float(amO), 2)
    amountPaid = round(float(amP), 2)
    
    if(amountPaid == amountOwed):
        print("No change. Amount paid equals amount owed.")
    elif(amountPaid < amountOwed):
        print("No change. Amount paid is less than amount owed.")
    else:
        calculateChange(amountOwed, amountPaid)
    
    
if __name__ == "__main__":
    main()