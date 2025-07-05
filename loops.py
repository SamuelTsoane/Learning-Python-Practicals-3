#Loops

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

numbers = [1, 2 ,3 ,4 ,5]

for number in numbers:
    print(number)
    
#Using a while loop to cout from 1 to 5

count = 1

while count <= 5:
    print(count)
    count += 1 #Increments hte count by 1
    
#Loop Control Statements

cars = ["Toyota", "BMW", "Mercedes", "Ford", "Honda"]

for car in cars:
    if car == "Ford":
        break #Exits the loop if Ford is found
    print(car)

print()
   
for car in cars:
    if car == "Ford":
        continue #Skips Ford and moves to the iteration
    print(car)
    
print()
   
for car in cars:
    if car == "Ford":
        pass #Placholder, no action is needed for Frod
    print(car)

count = 0
   
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break #Exits the loop when the count is reached