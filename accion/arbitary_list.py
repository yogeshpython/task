import random 

def RandGen(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
  
    return res 
  
# Driver Code 
num = int(input("Please enter number length"+" "))
start = int(input("Please enter starting number"+" "))
end = int(input("Please enter ending number"+" "))
print(RandGen(start, end, num)) 
