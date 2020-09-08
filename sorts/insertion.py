from main import main

def insertion_sort(array):
    array=array[:]
    for i in range(1,len(array)):
        key=array[i]
        for j in range(i-1,-1,-1):
            if array[j]>key:
                array[j],array[j+1]=array[j+1],array[j]
            else:
                break
    return array

if __name__=="__main__":
    main(insertion_sort)
