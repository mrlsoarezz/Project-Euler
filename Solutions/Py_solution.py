
def checkIt(number):
    if (number % 3 == 0 or number % 5 == 0):
        return True
    return False
    
def main():
    sum = 0
    
    for i in range(3, 1000):
        if checkIt(i):
            sum += i
            
    print(f"sum: {sum}")

main()
