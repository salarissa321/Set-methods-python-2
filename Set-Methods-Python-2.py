


#-----------------------
#---Set Methods-----
#-----------------------


# Difference()

a = {1,2,3,4,5,6}
b = {"Salar" , 1 , "Issa" , 2 , 3}

print(a) # {1, 2, 3, 4, 5, 6}
print(a.difference(b)) # {3, 4, 5, 6} # {4, 5, 6}
print(a) # {1, 2, 3, 4, 5, 6} # 

print("=" * 40) # separator ========================================


# difference Upadate()

c = {1,2,3,4,5,6}
x = {"Salar" , 1 , "Issa" , 2 , 3}

print(c) # {1, 2, 3, 4, 5, 6}
c.difference_update(x) 
print(c) # {4, 5, 6}


print("=" * 40) # separator ========================================


# intersection()

e = {1,2,3,4, "X"}
f = {"Salar" , 2 , "X"}
print(e) # {1, 2, 3, 4, 'X'}
print(e.intersection(f)) # {'X', 2}
print(e) # {1, 2, 3, 4, 'X'}


print("=" * 40) # separator ========================================


# intersection_update()

t = {1,2,3,4, "X"}
g = {"Salar" , 2 , "X"}
print(t) # {1, 2, 3, 4, 'X'}
print(t.intersection_update(g)) 
print(t) # {2, 'X'}


print("=" * 40) # separator ========================================


# Symmetric_difference()


i = {1,2,3,4,5,6,7, "X"}
v = {"Salar" , 1, 3, 5 , "Issa"}
print(i) # {1, 2, 3, 4, 5, 6, 7, 'X'}
print(i.symmetric_difference(v)) # {2, 4, 'Issa', 7, 6, 'X', 'Salar'}
print(i) # {1, 2, 3, 4, 5, 6, 7, 'X'}


print("=" * 40) # separator ========================================

# Symmetric_difference_update()

l = {1,2,3,4,5,6,7, "X"}
s = {"Salar" , 1, 3, 5 , "Issa"}
print(l) # {1, 2, 3, 4, 5, 6, 7, 'X'}
print(l.symmetric_difference_update(s)) 
print(l) # {2, 4, 6, 7, 'Issa', 'X', 'Salar'}



