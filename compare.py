#!/usr/bin/python

import random
import numpy as np
from datetime import datetime 
import time
import timeit
import matplotlib.pyplot as plt
from insertionSort import insertionSort
from mergeSort import mergeSort
from heapSort import heapSort
from quickSort import quickSort
from modifiedQuickSort import modifiedQuickSort


def calculateAvg(func,execTime,INPUT_SIZE,sorting_type):

    FuncName = {
        'insert':insertionSort,
        'merge':mergeSort,
        'heap':heapSort,
        'quick':quickSort,
        'modifiedQuick':modifiedQuickSort

    }
    #### Should be Taking average for 3 dataset
    Num_Of_Case = 1
    timeElapsed = 0
    sortingName = FuncName[func]
    #alg = FuncName.get(func,lambda:"Invalid Function")

    data_type = {
        1: "_sorted",
        2: "_reverse",
        3: ""
    }

    for i in range(1,Num_Of_Case+1) :
        arr = []
        inputFile = open("DataSet/dataSet" + str(i) + data_type.get(sorting_type) + ".txt", "r")
        arr = np.loadtxt(inputFile,dtype=int,max_rows=INPUT_SIZE)
        #print(arr)
        inputFile.close()
        startTime = time.time()
        sortingName(arr,0,len(arr)-1)
        timeElapsed = timeElapsed + time.time()-startTime
        outputFile = open("Result/"+func+"_"+str(INPUT_SIZE)+"_"+str(i)+".txt","w")
        outputFile.writelines("%s\n" %item for item in arr)
        outputFile.close()
    timeElapsed = timeElapsed/Num_Of_Case
    execTime.append(timeElapsed)
    print ('Time elapsed in Execution of '+func+' : '+str(timeElapsed)+'seconds')

def main() :

    # print("Select Sorting Algorithm to test :")
    # print("1. Insertion Sort")
    # print("2. Merge Sort")
    # print("3. Heap Sort")
    # print("4. In-Place Quick Sort")
    # print("5. Modified Quick Sort")
    # print("6. All Sorting Algorithms")
    print("1. sorted")
    print("2. reversely sorted")
    print("3. Random inputs")
    sorting_type = int(input("how do you want the inputs to be:"))
    func = []
    # while len(func)==0 :
    # 	algorithm = input("Enter the Algorithm number :")
    # 	if algorithm ==6 :
    # 		func = [item for item in range(1,7)]
    # 		break
    # 	if (algorithm>=1 or algorithm<=5) :
    # 		func.append(algorithm)
    # 		break
    # 	print("Please Enter valid Input")
    # print("selected:",func)
    #

    size = [1000,2000,3000,4000,5000,10000,20000,30000,40000,50000]
    #size = [1000]
    #print("Random Genaration of DATASET started")

    #for num in range(1,4):
    #	INPUT_SIZE = 50000
    #	inputFile = open("DataSet/dataSet"+str(num)+".txt","w")
    #	inputFile.writelines("%s\n" %random.randint(0,INPUT_SIZE) for x in range(0,INPUT_SIZE))
    #	inputFile.close()

    print("Random Genaration of DATASET Ended --")

    insert = []
    merge = []
    heap = []
    quick = []
    modifiedQuick = []

    for num in size:
        print("\n For input size of :"+str(num))
    #	calculateAvg('insert',insert,num, sorting_type)
        calculateAvg('merge',merge,num, sorting_type)
        calculateAvg('heap',heap,num, sorting_type)
        calculateAvg('quick',quick,num, sorting_type)
    #	calculateAvg('modifiedQuick',modifiedQuick,num, sorting_type)

    print(insert)
    print(merge)
    print(heap)
    print(quick)
    print(modifiedQuick)

    #plt.plot(size, insert, label = "Insertion Sort")
    plt.plot(size, merge, label = "Merge Sort")
    plt.plot(size, heap, label = "Heap Sort")
    plt.plot(size, quick, label = "Quick Sort")
    #plt.plot(size, modifiedQuick, label = "Modified Sort")
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Two lines on same graph!')
    plt.legend()
    plt.show()

if __name__ == "__main__" :
    main()
