#INSERSTION SORT ALGORITHM

def insertionSort(arrayOne): 
    count = 0

    for i in range(1, len(arrayOne)):
        valueSorted = False
        count = i
        while arrayOne[count] < arrayOne[count-1] and count != 0:
            # Swaps the two values
            temp = arrayOne[count]
            arrayOne[count] = arrayOne[count-1]
            arrayOne[count-1] = temp
            count -= 1         

    return arrayOne

arrayToSort = [9,2,7,4,5,3]

print("The sorted array is : ", insertionSort(arrayToSort))
