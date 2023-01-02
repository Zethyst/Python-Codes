dic={
    "Akshat":"Human Being",
    "Spoon":"Object" 
}
print(dic["Akshat"])

employees={
    665:"Harshita",
    646:"Akshat",
    644:"Adrija",
    119:"Akash"
}
print(employees[665]) #663 raises error

print(employees.get(663))  #663 doesn't raise error

print(employees.values())
print(employees.keys())
print(employees.items())

for key in employees.keys():
    print(f"The Employee associated with {key} is {employees[key]}")
    
for key, value in employees.items():
  print(f"The value corresponding to the key {key} is {value}") 
  