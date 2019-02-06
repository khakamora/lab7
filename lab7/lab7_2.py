'''
Created on 6 лют. 2019 р.

@author: F
'''
d = {}
with open("students.csv") as file:
    for line in file:
        key, *value = line.split()
        d[key] = value
        
print(d)