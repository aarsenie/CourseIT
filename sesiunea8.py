# RECAP

#ex 17:
# Given the list = ["one", "two", "three"]
# what should we write to get the string "one-two-three"?
lst = ["one", "two", "three"]
res_str = "" # variabila in care vom construi rezultatul (concatenarea respectiva)
for i in lst:
        res_str += i + "-"
# res_str = res_str.strip('-')
res_str = res_str[:-1]
print(res_str)

# v3 - cu join
print("-".join(lst))
# poti face join prin ceva ce se itereaza (lst, tupla, etc)

print("-".join("alphabet"))

#Recap18:

#Recap19:

#given two lists: lst1 = [1,2,3,4], lst2 = [9,8,7,6].
#write a piece of code to iterate both lists simutaneously and display items from lst1 in original order
# and items from lsts2 in reverse order.
lst1 = [1,2,3,4]
lst2 = [9,8,7,6]

lst2_rev = list(reversed(lst2))
print(lst2)

for i in range(0,len(lst1)):
        print(lst1[i], lst2_rev[i])

#v2
for i in zip(lst1, reversed(lst2)):
        print(i)

#Recap20:
# What will the following code return?
def func(a, b=22):
        c = 'abc'
        return a,b,c
t1, t2, t3= func(11)
print(t1)
print(t2)
print(t3)

#Recap21: What will the following code return?
n = 100
def f():
        n = 45 # are sens doar in functie
        return n
f()
print(n)

#Recap22:
n = 100
def f():
        global n #definind in interiorul functiei pe n ca fiind global,
                # se echivaleaza cu variabila de mai sus
        print(n)
        n = 45
f()
print(n)


lst = [5, 10, 15, 20, 25]
print(lst[::-2])

#Recap25:
#How to begin to write to loop that will run forever?

ture_de_facut = 5
while ture_de_facut > 0: #returneaza True/False
        print("Am mai facut o tura")
        ture_de_facut -= 1

while 5 != 0: #ruleaza la infinit
         pass
# while True:
#         pass
# #ruleaza la infinit
#         print("Ruleaaz la infinit")
#         break

##discutii TEMA7

# from abc import ABC
#
# class FormaGeometrica(ABC)
#         def __init__(self):




