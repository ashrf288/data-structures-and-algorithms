

def QuickSort(arr,left,right):
    if left < right:
   #Partition the array by setting the 
   # position  of the pivot value
       position=Partition(arr,left,right)
       # Sort the left
       QuickSort(arr, left, position - 1)
       #Sort the right
       QuickSort(arr, position + 1, right)
    return arr
def Partition(arr,left,right):
    pivot=arr[right]
    low=left-1
    for i in range(left,right):
        if arr[i]  <= pivot :
           low+=1
           swap(arr,i,low)
    swap(arr,right,low +1)
    return low +1


def swap(arr,i,low):
    temp= arr[i]
    arr[i]=arr[low]
    arr[low]=temp



print(QuickSort([8,4,23,42,16,15],2,5))