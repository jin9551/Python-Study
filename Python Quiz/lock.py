#!/usr/bin/env python3
#lock.py written by Jinha Jeong
#pep605


import re
import sys

#check if the given clues are invalid
def invalidClue(args):
    invalid=list()
    count=0
    c=sys.argv[1:].copy()
    for i in range(len(c)):
        r=re.match('^[0-9]{3}\-[0-3]\-[0-3]$', c[i])
        try:
            #this will through AttributeError, so force it to append the invalid clues:/
            if(r.group() != c[i]):
               invalid.append(c[i])
        except AttributeError:
               invalid.append(c[i])
               count += 1
    return count,invalid

#function to split sys.argv into usable variables    
def splitThem (raw_clue):
    a = list ()
    b = list ()
    c = list ()
    for i in range (len (raw_clue)):
        temp = raw_clue[i].split ('-')
        a.append (temp[0])
        b.append (temp[1])
        c.append (temp[2])
    return (a, b, c) 

#function to solve puzzle
def lockSolve(number, checknumber, right, wrong):
    count_right=0
    count_wrong=0
    comp_number=str(number).zfill(len(checknumber))
    for i in range(len(checknumber)):
        if comp_number[i] == checknumber[i]:
            count_right += 1
        if comp_number[i]!= checknumber[i] and comp_number[i] in checknumber:
            count_wrong += 1
    return right==count_right and wrong == count_wrong

            
            
#check and return the invalid clue list
(z,y)=invalidClue(sys.argv)
#list of clues
x=sys.argv[1:].copy()



#if no clues are given
if(len(x)==0):
    print("Need to give some patterns of the form XYZ-R-W")
    sys.exit()

#if all of the clues are valid print them in one line, otherwise print the invalid clues and terminate
if(z==0): 
    print("Trying", end=' ')
    for i in range(len(x)):
        print(x[i], end=' ')
    print()        
else: 
    print("Invalid argument:", end=' ')
    for i in range(len(y)):
        print(y[i], end=' ')
    sys.exit()


#split clues
(XYZ, R, W) = splitThem(x) 

#for digit1 in range(10):
    #for digit2 in range(10):
        #for digit3 in range(10):
            #i = str(digit1)+str(digit2)+str(digit3)

solution_count=0
noSolution=0
              
for i in range(1000):
    arg_count=0  
    while(arg_count < len(x)):
            #number=str(digit1)+str(digit2)+str(digit3)      
        if lockSolve(i, XYZ[arg_count], int(R[arg_count]), int(W[arg_count])) and (arg_count == len(x)-1):
            solution_count += 1
            noSolution += 1
            print("*** Soultion #%d is " % solution_count,end='')
            print(str(i).zfill(3))
            break
        elif lockSolve(i, XYZ[arg_count], int(R[arg_count]), int(W[arg_count])):
            arg_count += 1
            continue
        else:
            break   
if noSolution == 0:
    print("No Solutions Found")




        