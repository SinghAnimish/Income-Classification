#Generate prime numbers between 100 to 300
  
for value in range(100,300): 
    if (value > 1): 
       for num in range(2, value): 
           if (value % num) == 0: 
               break
       else: 
            print(value) 
    

