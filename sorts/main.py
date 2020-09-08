def main(func):
    size=int(input("Enter the size of the array: "))
    array=[int(input(f"Enter {i+1} element: ")) for i in range(size)]
    sorted_array=func(array)
    print(f"sorted array: {sorted_array}")
