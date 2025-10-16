name = ["Nahom","Shem","Biruk"]

def stud(f,x):
    f(x)
    
def namep(x):
    print("Hello",x)


for i in range(len(name)):
    stud(namep,name[i])

#################################################################################################

def op(num1, num2, s):
    for x in s:
        print(f"{num1} {x} {num2} = ", eval(str(num1)+x+str(num2)))

operations = ['+','-','/','*']
op(5,4,operations)

#################################################################################################




