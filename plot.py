import matplotlib.pyplot as plt

#function to read a file from timings folder
def read_file(filename):
    dir="./timings/"
    file = open(dir+filename,"r")
    lengths=[]
    times=[]
    for line in file:
        words=line.strip().split(",")
        lengths.append(int(words[0]))
        times.append(float(words[1]))
    return lengths,times

#function to plot the graph
#it takes a list of tuples containing,
#lengths of arrays
#time required to sort
#name of sort
#the second parameter is size, the max size of array to be plotted
def subplot(xyname,size=None):
    if size is None:
        for x,y,name in xyname:
            plt.plot(x,y,label=name)
            size=x[-1]
    else:
        for x,y,name in xyname:
            if name!="Counting":
                plt.plot(x[:size],y[:size],label=name)
    plt.legend()
    plt.xlabel("Number of elements")
    plt.ylabel("Time for execution (microseconds)")
    plt.title(f"Max Array Size: {size} Elements")

#function to read all the files and pair them with the name of the sorts
def get_data(sorts):
    xyname=[]
    for sort in sorts:
        x,y=read_file(sort.__name__+".txt")
        name=" ".join(sort.__name__.split("_")[:-1]).title()
        xyname.append((x,y,name))
    return xyname

#the main plot function that calls all the other functions
def plot(sorts):
    xyname=get_data(sorts)
    plt.subplot(2,1,1)
    subplot(xyname,100)
    plt.subplot(2,1,2)
    subplot(xyname)
    plt.show()


