# PYTHON IF-ELSE

if __name__ == '__main__':
    n = int(raw_input().strip())
range1 = range(2,5)
if n%2 == 1:
    
    print("Weird")
    
if n%2 == 0 and n in range(2,6):
    
    print("Not Weird")
elif n % 2 == 0 and n in range(6,21):
    
    print("Weird")
elif n%2 == 0 and n > 20:
    print("Not Weird")


    
# ARTHMETIC OPERATORS

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
print(a+b)
print(a-b)
print(a*b)   


# PYTHON DIVISION

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print(a//b)
print(a/b)

# LOOPS

if __name__ == '__main__':
    n = int(input())

for i in range(n):
    
    print(i**2)

# WRITE FUNCTION

def is_leap(year):
    
   
    if year%100==0:
        if year%400 == 0:
            return True
        else:
            return False
    elif year%4 == 0:
        return True
    else:
        return False
    # Write your logic here
    
    return leap


# FIND RUNNER UP SCORE!

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    ns = set(arr)
    
    ns.remove(max(ns))
    
    print(max(ns))




# NESTED LISTS

if __name__ == '__main__':
    
    
    #create dicitionary
    # put the nested list into dictionary
    # after that return dict.values()
    #maybe from that retrieve the keys
    
    records = []
    for _ in range(int(raw_input())):
        
        name = raw_input()
        score = float(raw_input())
        records.append([name,score])
    #print(records)   
    # return records

    # for i in range(len(records)):
        
    #     for j in range(len(i)):
            
    #         if records[i][0] == :
                
    #             themax = max(themax,maxtrack)
    
    dic = {re[0]:re[1] for re in records}
    
    new = dic.values()
    first = set(new)
    second = sorted(first)[1]
    
    third = [k for k,v in dic.items() if v == second]
    third.sort()
    
    for el in third:
        print(el)
    
    
#finding percentage

from decimal import Decimal
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    find = student_marks[query_name]
    
    tot = sum(find)
    avgd = Decimal(tot/3)

    print("{:.2f}".format(avgd))    
                
                
#lists

if __name__ == '__main__':
    N = int(raw_input())
 
       
    #command = li
  
    l = []
    for _ in range(N):
        s = raw_input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("l."+cmd)
        else:
            print l
   

#tuples

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    tup = tuple(integer_list)
    print(hash(tup))
   

#swapecase

def swap_case(s):
    li = []
    stri = ""
    for i in s:
        #print(i)
        if i.islower():
            i = i.upper()
            li.append(i)
            
        elif i.isupper():
            i = i.lower()
            li.append(i)
        else:
            li.append(i)
            
    return stri.join(li)
     
    
    

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result

#string split and join

def split_and_join(line):
    
    line = line.split(" ")
    line = "-".join(line)
    
    return line
    
    
    # write your code here

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result


#what is your name?
# Michael

def print_full_name(first, last):
    # Write your code here
    print("Hello " + str(first) + " " + str(last) + "!" + " " + "You just delved into python.") 

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)


#mutations 

def mutate_string(string, position, character):
    
    string  = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new


# find a string 

def count_substring(string, sub_string):
    count = 0
    
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            # result = string.find(sub_string)
            count +=1
    return count
    #for i in range(len(string)):
    print(c) 

#symmetric

m=int(input())
a=set(map(int,input().split()))
n=int(input())
b=set(map(int,input().split()))
for i in sorted(a.symmetric_difference(b)):
    print(i)
#set add

print(len(set([str(input()) for _ in range(int(input()))])))

#discard,remove,pop

choice=input().split()
if choice[0]=="pop" :
    s.pop()
elif choice[0]=="remove" :
    s.remove(int(choice[1]))
elif choice[0]=="discard" :
    s.discard(int(choice[1]))

    #or
n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))

# set union

_,set1 = input(), set(input().split())
_,set2 = input(), set(input().split())



print(len(set1|set2))


# no idea


n, m = input().split()

ar = input().split()
import math

a = int(input())
b = int(input())
m = int(input())

print(pow(a,b))
print(pow(a,b)% m)
A = set(input().split())
B = set(input().split())
c= sum([(i in A) - (i in B) for i in ar])
print(c)

#mod divmod

from __future__ import division

a = int(input())
b = int(input())

print(a//b)
print(a%b)
print(divmod(a,b))

# power mod power

import math

a = int(input())
b = int(input())
m = int(input())

print(pow(a,b))
print(pow(a,b)% m)


# find angle mbc

import math

ab = int(input())
bc = int(input())

# ac = math.sqrt(ab**2 + bc**2)
# M = ac/2
# bm = math.sqrt(bc**2 - M**2)
# deg = bm/bc
# degb = 3.14159 - 1.5708 - deg
# print(round(math.degrees(degb)))

print(round(int(math.degrees((math.atan2(bc,ab))))))


# product

from itertools import product
A = list(map(int,input().split(' ')))
B = list(map(int,input().split(' ')))


print(*product(A,B))

# PERMUTATION
from itertools import permutations
n = input().split(' ')
#print(n[0])
per = sorted(list(permutations(n[0],int(n[1]))))

[print("".join(i)) for i in per]


#combination

from itertools import combinations
n = input().split(' ')
#print(n[0])
li = list(n[0])
n1 = int(n[1])
per = sorted(list(combinations(li,int(n[1]))))
#print(per)
for i in range(1,n1+1):
    
    for j in combinations(sorted(li),i):
        print("".join(j))
   # [print("".join(j)) for j in per]


#COMPRESS STRING --- GROUPBY()

from itertools import groupby

for k,c in groupby(input()):
    print((len(list(c)),int(k)))


#ITERABLES AND ITERATORS

from itertools import combinations;
n = int(input().strip())
m = input().strip().split()
z = int(input().strip())

ag = 0
all=0
for i in combinations(m,z):
    all+=1
    if 'a' in i:
        ag=ag+1
        
print(ag/all)


# from itertools import combinations
# import itertools

# n= int(input())
# m = input().split()
# z =  input()

# li = []
# for i, el in enumerate(m):
#     if el == "a":
#         li.append(i+1)
  
# c = tuple(combinations(range(1,n+1), int(z)))
# fc = [a_tuple[0] for a_tuple in c]
# result = [i for i in fc if i in li]
# r = len(result)
# print(r/len(c))



# COUNTER

from collections import Counter

m = input()
sizec = Counter(map(int,input().split()))
c= int(input())

income = 0

for i in range(c):
    c1,c2 = map(int,input().split())    

    if sizec[c1]:
        income += c2
        sizec[c1] -=1
        
        
print(income)



#ATHLETE SORT



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])
    
    
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        
        

    k = int(input())
    
   
    arr.sort(key=lambda x: x[k])
    
    for el in arr:
        print(*el)


# DEFAULT DICT TUTORIAL

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n = input().split()



# create a list and append group A values with default key mechanism
# the key in the dic is the letter and value is the position
# (key,[value])
#
d= defaultdict(list)
list1 = []

for i in range(0,int(n[0])):
    
    d[input()].append(i+1)
    
    
    
for i in range(int(n[0]), int(n[0])+int(n[1])):
    list1.append(input())
    
# print(list1)
for i in list1:
    if i in d:
        print( " ".join(map(str,d[i])))
        
    else:
        print(-1)
        

#traingle quest 

for i in range(1,int(input())+1):
    print(((10**i-1)//9)**2)


# NAMED TUPLES

from collections import namedtuple


m = input()
n = str(input())

col = namedtuple("col",n)
s = 0
for i in range(int(m)):
    z = input().split() 
    c = col(*z)
    s += int(c.MARKS)
print(s/int(m))


# ORDERED DIC

# items with price tag 
# return item name

# read each item then multiply it with the total occurance
from collections import OrderedDict

m = int(input())

o_dic = OrderedDict()

for i in range(m):
    
       
   
    
    name = input().split()
    k = ' '.join(map(str,([x for x in name if not x.isdigit()])))
    
    v = int([x for x in name if x.isdigit()][0])
    
    if k in o_dic:
        v += o_dic[k]
        o_dic[k] = v
    o_dic[k] = v


for k,v in o_dic.items():
    print(k, v)




# DEQUE

from collections import deque

d = deque()


for i in range(int(input())):
    method,*n = input().split()
    
    getattr(d,method)(*n)
    
print(*d)
    
 

#EXCEPTION


m = input()


for i in range(int(m)):
    try:
        a,b = map(int,input().split()) 
        division_result = a // b
        print(division_result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)



#REGEX

import re

t = int(input())

for i in range(t):
    
    s = input()
    try:
        re.compile(s)
        print(True)
        
    except:
        print(False)
    


import math

# Ax = 0, Bx = 1, Cx = 0, Dx = 1

# Ay = 4, By = 7, Cy =5 , Dy = 7

# Az = 5, Bz = 6, cz = 9, Dz = 2



class Points(object):
    def __init__(self, x, y, z):
        
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        
        return Points((self.x-no.x),(self.y-no.y),(self.z-no.z))

    def dot(self, no):
        
       return  self.x * no.x + self.y*no.y + self.z*no.z

    def cross(self, no):
        
         return Points((self.y*no.z-self.z*no.y),(self.z*no.x-self.x*no.z),(self.x*no.y-self.y*no.x))        
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


# ZIPPED

m,n = map(int,input().split())

li = []

for i in range(n):
    
    li.append(map(float,input().split()))
    

for i in zip(*li):
    
    print(sum(i)/len(i))


# ANY OR ALL

m = int(input())

n = input().split()

def palandimor(x):
    if x[::-1] == x:
        return True
    
    else:
        return False




print(all([int(i) > 0 for i in n]) and any([palandimor(el) for el in n]))
