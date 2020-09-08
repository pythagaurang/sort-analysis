from main import main

def selection_sort(array):
    array=array[:]
    length=len(array)
    for i in range(0,length):
        minimum=i
        for j in range(i+1,length-1):
            if array[j]<array[minimum]:
                minimum=j
        array[i],array[minimum]=array[minimum],array[i]
    return array

if __name__=="__main__":
    main(selection_sort)
