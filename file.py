print("Welcome To My Program")
print("Calculator")
print("Choose an option:\n1.Add\n2.Subtract")
option = int(input("Enter Your Option here: "))
print("You Choosed: ", option)
if option == 1:
        
    num1 = float(input("Enter 1st Number"))
    num2 = float(input("Enter 2nd Number"))
    print("The sum is", num1 + num2)

else:
    print("Wrong Option")    