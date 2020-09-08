from main import main

def quicksort_m(array,low,high):
    if low<high:
        mid=(low+high)//2
        i=low
        j=high
        pivot=array[mid]
        while True:
            while array[i]<pivot:
                i+=1
            while array[j]>pivot:
                j-=1
            if i>=j:
                break
            array[i],array[j]=array[j],array[i]
        quicksort_m(array,low,j)
        quicksort_m(array,j+1,high)
    return array

def quicksort_h(array,low,high):
    def partition(array,low,high):
        i=low
        pivot=array[high]

        for j in range(low,high):
            if array[j]<=pivot:
                array[j],array[i]=array[i],array[j]
                i+=1
        array[i],array[high]=array[high],array[i]
        return i
    if low<high:
        pivot = partition(array,low,high)
        quicksort_h(array,low,pivot-1)
        quicksort_h(array,pivot+1,high)
    return array

def quicksort_l(array,low,high):
    def partition(array,low,high):
        i=high
        pivot=array[low]
        for j in range(high,low,-1):
            if array[j]>=pivot:
                array[j],array[i]=array[i],array[j]
                i-=1
        array[i],array[low]=array[low],array[i]
        return i
    if low<high:
        pivot = partition(array,low,high)
        quicksort_l(array,low,pivot-1)
        quicksort_l(array,pivot+1,high)
    return array
    

def quick_middle_sort(array):
    sorted_array=quicksort_m(array,0,len(array)-1)
    return sorted_array
def quick_high_sort(array):
    sorted_array=quicksort_h(array,0,len(array)-1)
    return sorted_array
def quick_low_sort(array):
    sorted_array=quicksort_l(array,0,len(array)-1)
    return sorted_array

if __name__=="__main__":
    main(quick_high_sort)
    main(quick_low_sort)
    main(quick_middle_sort)

