from main import main

def counting_sort(array):
    mini,maxi=min_max(array)
    length=len(array) 
    count=[0 for i in range(mini,maxi+1)]
    
    for i in range(length):
        count[array[i]-mini]+=1
    
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    
    i=length-1
    sorted_a=[0]*length
    
    while i>=0:
        sorted_a[count[array[i]-mini]-1]=array[i]
        count[array[i]-mini]-=1
        i-=1
    return sorted_a

def min_max(array):
    mini=array[0]
    maxi=array[0]
    for elem in array:
        if mini>elem:
            mini=elem
        if maxi<elem:
            maxi=elem
    return mini,maxi

if __name__=="__main__":
    main(counting_sort)
