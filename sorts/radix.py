from main import main

def counting_sort(array,exp):
    length=len(array)

    count=[0]*10
    
    for elem in array:
        count[(elem//exp)%10]+=1
    
    for i in range(1,10):
        count[i]+=count[i-1]
    
    i=length-1
    sorted_a=[0]*length
    
    while i>=0:
        index =(array[i]//exp)%10
        sorted_a[count[index]-1]=array[i]
        count[index]-=1
        i-=1
    
    for i in range(length):
        array[i]=sorted_a[i]

    return sorted_a

def maximum(array):
    maxi=array[0]
    for elem in array:
        if maxi<elem:
            maxi=elem
    return maxi

def radix_sort(array):
    maxi=maximum(array)
    exp=1
    while maxi//exp>0:
        counting_sort(array,exp)
        exp*=10
    return array

    
if __name__=="__main__":
    main(radix_sort)
