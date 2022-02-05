# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:10:03 2021

@author: lucijacovic
"""

#234(5), 300(2), 950(4), 109(3), 419(8), 777(10), 876(7), 796(8)

def main():
    start=int(input("Any number from 1 to 1000: "))
    n=str(start)
    print("Longest sequence:", longestSequence(n))

def longestSequence(n):
    current=0

    # bazni slucaj(inace beskonacno): broj jednoznamenkast (nema smisla razbijati na manje)
    if len(n)==1:
        return max(current, 1)
    
    if len(n)==4: #jedino 1000
        return max(current, 2)  #(1000,0)
    
    for i in range(len(n)-1): #2,34  23,4
        a=n[0:i+1] #string slicing
        b=n[i+1:]
        multiply=str(int(a)*int(b)) # 2 * 34 = 68, 23 * 4 = 92
        current=max(current, 1 + longestSequence(multiply)) #recursion
    
    for i in range(len(n)-2): #2,3,4
        for j in range(i+1, len(n)-1):
            a=n[0:i+1] #string slicing
            b=n[i+1: j+1]
            c=n[j+1:]
            multiply=str(int(a)*int(b)*int(c)) # 2 * 3 * 4 = 24
            current = max(current, 1 + longestSequence(multiply)) #recursion
            
    return max(current, 1 + longestSequence(multiply))

if __name__ == "__main__":
    main()
