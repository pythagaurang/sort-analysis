from main import main
    
def merge(array1,array2):
    l_1=len(array1)
    l_2=len(array2)
    array3=[]
    i=j=0
    while(i<l_1 and j<l_2):
        if array1[i]<array2[j]:
            array3.append(array1[i])
            i+=1
        elif array1[i]>array2[j]:
            array3.append(array2[j])
            j+=1
        else:
            array3.append(array1[i])
            array3.append(array2[j])
            i+=1
            j+=1
    while i<l_1:
        array3.append(array1[i])
        i+=1
    while j<l_2:
        array3.append(array2[j])
        j+=1
    return array3

def merge_sort(array):
    if len(array)<=1:
        return array
    else:
        mid=len(array)//2
        return merge(merge_sort(array[:mid]),merge_sort(array[mid:]))
    

if __name__=="__main__":
    main(merge_sort)
