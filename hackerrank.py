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

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split()

ar = input().split()

A = set(input().split())
B = set(input().split())
c= sum([(i in A) - (i in B) for i in ar])
print(c)