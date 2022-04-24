import random
i = 0
incircle = 0
outcircle = 0
while i < 1000000:
    x =  random.uniform(0,1)
    y = random.uniform(0,1)
    if x*x + y*y >= 1:
        #not in circle
        outcircle += 1
    else:
        #in circle
        incircle += 1
    i += 1
piover4 = incircle/(incircle+outcircle)
pi = 4*piover4
print(pi)