inc = float(input("Please Enter Your Income: "))

def calculate_tax(inc,rate):
    if rate == "err":
        print("Please Enter a valid income amount")
    else:
        tax_amount = inc*rate
        net_income = inc - tax_amount
        print(f"Your tax amount is {tax_amount} and net income is {net_income}. ")


if inc>=0 and inc<=2000:
    print("You're tax free.")

else:
    calculate_tax(inc,(lambda x : 0.15 if inc<= 4000 else ( 0.2 if inc<= 7000 else (0.25 if inc<= 10000 else ( 0.3 if inc<=14000 else ( 0.35 if inc>14000 else "err")))))(inc))