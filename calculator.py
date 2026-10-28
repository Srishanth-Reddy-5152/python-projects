# calculator
num_1=int(input("enter num 1:  "))
num_2=int(input("enter num 2:  "))

opp = (input("Enter desired oppration  : "))
if (opp =="+"):
    print(f"solution = {num_1+num_2}")
elif(opp =="-"):
    print(f"solution = {num_1-num_2}")
elif(opp =="*"):
    print(f"solution = {num_1*num_2}")
elif(opp == "/"):
    print(f"solution = {num_1/num_2}")
