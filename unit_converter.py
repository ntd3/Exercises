import requests
print("""
##################################################################################
      
                             Simple Unit Converter                                   

##################################################################################       
      
      Options:
              1. Celsius to Farenheit
              2. Farenheit to Celsius 
              3. Meter to Centimeter
              4. Centimeter to Meter
              5. USD to ETB ( Real Time ) 
              
              
""")


def c2f(x):
    calc = (x * 1.8) + 32
    unit = "Farenheit"
    return calc, unit

def f2c(x):
    calc = (x - 32) / 1.8
    unit = "Celsius"
    return calc, unit

def m2c(x):
    calc = x*100
    unit = "Centimeters"
    return calc,unit

def c2m(x):
    calc = x/100
    unit = "Meters"
    return calc,unit

def u2e(x):
    
    url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert"

    querystring = {"from":"USD","to":"ETB","amount":"1"}

    headers = {"x-rapidapi-host": "currency-conversion-and-exchange-rates.p.rapidapi.com","x-rapidapi-key":"51b3442dc5msh9433570f6c935a5p18c769jsn150485c1fb64"}

    response = requests.get(url, headers=headers, params=querystring)

    rate = response.json()['info']['rate']
    calc = x * rate
    unit = "ETB"
    return calc,unit
choice = int(input("Plese Enter Your Choice: "))
unit1 = float(input("Please enter the value: "))
match choice:
    case 1:
        calc,unit = c2f(unit1)
    case 2:
        calc, unit = f2c(unit1)
    case 3:
        calc,unit = m2c(unit1)
    case 4:
        calc, unit = c2m(unit1)
    case 5:
        calc, unit = u2e(unit1)

print(f"The value you entered is {round(calc,2)} {unit}")