#Ejercicio1

for x in range(151):
    print(x)

#Ejercicio 2 
for x in range(5,1005,5):
    print(x)

#Ejercicio 3
def declaraciones(q, z):
    for x in range(1, 101): 
        print(x)
        if x % q == 0:
            print("Coding")
        if x % z== 0:
            print("Coding Dojo")
        else:
            print(x)
    
declaraciones(5, 10)


#Ejercicio 4
total=0
for j in range(0, 500):

    print(j)
    if j % 2 == 1 :
        
        total+=j

print(total)


#Ejercicio 5
print("-------------")
print("EJERCICIO 5")
for num in range(2019,1,-4):
    print(num)


#Ejercicio 6
lowNum = 1
highNum = 8
mult = 2 

for num in range(lowNum, highNum):
    if num % mult == 0:
        print(num)


        