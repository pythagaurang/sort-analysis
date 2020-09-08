from main import main

def bubble_sort(array):
    array=array[:]
    for i in range(len(array)-1,0,-1):
        for j in range(0,i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

if __name__=="__main__":
    main(bubble_sort)
