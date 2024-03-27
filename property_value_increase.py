property_initial = int(input("What is the value of the property? "))
perc = int(input("By what percentages does the value increase per year?"))
year = 0

property = property_initial 
while property_initial < property:
    property_initial = property_initial * (1 + perc / 100)
    print("Year", year, "-", property_initial)
    year += 1
 
