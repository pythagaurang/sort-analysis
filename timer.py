#this is a code 

import random
from time import time_ns
import math
import plot
#importing all the sorts
from sorts.merge import merge_sort
from sorts.insertion import insertion_sort
from sorts.bubble import bubble_sort
from sorts.selection import selection_sort
from sorts.counting import counting_sort
from sorts.quick import quick_high_sort
from sorts.radix import radix_sort

#sorts divided by complexity
allsorts=[insertion_sort,merge_sort,bubble_sort,selection_sort,quick_high_sort,radix_sort,counting_sort]
allsorts_c=[insertion_sort,merge_sort,bubble_sort,selection_sort,quick_high_sort,radix_sort]
lognsorts=[merge_sort,quick_high_sort,radix_sort]
nsqrsorts=[insertion_sort,bubble_sort,selection_sort]

#select the sorts that you want to analyse
sorts=allsorts_c
#change min_r,max_r to see how it effects counting sort
min_r=0
max_r=100000
def array_size():
#maximum size of the array to be analyzed
    size=int(input("Enter the max array size for analysis (>100): "))
    if size>100:
        size=math.ceil(math.log(size,10)) # saving the size as nearest
                                          # larger power of 10
    else:
        size=2 #10**2=100
    print(f"The max array size: {10**size}")
#create an array of sizes from 1 to user input size there 
#will be 100 data points for each power of 10
#i.e 100: 1-100(step=1), 1000: 100-1000(step=10) and so on.
    sizes=[]
    for i in range(2,size+1):
        sizes+=[*range(10**(i-2),10**i,10**i//100)] 
    sizes.append(10**size)
    return size,sizes

random.seed(42)

#array generator for memory management
def array_gen(sizes):
    for size in sizes:
        yield [random.randint(min_r,max_r) for i in range(size) ]

#function for timing the sorts
def func_timer(func,*args):
    times=[]
    for i in range(100):
        time=time_ns()
        output=func(*args)
        time=time_ns()-time
        time=time/10**3
        times.append(time)
    return sum(times)//len(times)

#function for writing length of the array and time required for execution
#to a file
def write_to_file(times,sortname):
    filename=sortname+".txt"
    filepath="./timings/"+filename
    file = open(filepath,"w")
    for length,time in times.items():
        file.write(str(length)+","+str(time)+"\n")

#function to print the loading animation and percentage
def loading(sortname,length):
    global size
    sortname=" ".join(sortname.split("_"))
    print("\r"+sortname.title()+":\t",end="",flush=True)
    loading_string=[".",".",".",".",".",".",".",".",".","."]
    for i in range(length//(10**(size-1))):
        loading_string[i]="#"
    print("[ "+" ".join(loading_string)+" ]"+f" {length//10**(size-2)}% {length} {size}",end="",flush=True)

#the main function that analyzes all the sorts for
#for array of size 1 to n and elemnts of range
#min_r(def:0) to max_r(def:100000)
def timer(sort):
    times={}
    for array in array_gen(sizes):
        length=(len(array))
        loading(sort.__name__,length)
        time= func_timer(sort,array)
        times[length]=time
    print()
    write_to_file(times,sort.__name__)

if __name__=="__main__":
    size,sizes=array_size()
    for sort in sorts:
        timer(sort)
    plot.plot(sorts)
