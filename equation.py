                             def is_perfect_cube(x):
                                  return int(round(x**(1./3))) ** 3 ==x
    
                              def calc():
                                  for i in range(100):
                                       y= (i**6) + 8*(i**4) -6*(i**2) +8
                                       if(is_perfect_cube(y)):
                                           print(i)
          
          
          
 
# the above code checks for x in range 0 -100 if it satisfies the above equation
 #and the first solution is found for x=3 and t=11
