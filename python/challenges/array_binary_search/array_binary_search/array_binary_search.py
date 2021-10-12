
def includes(arr,n):
    """ 
     this function takes two argument one array sorted and the second is a num
     and will return the the index of the num if it was in the array 
     else it willl return -1
     
    """
    # for every binary search locate start and mid and end and then iterate thorw thm to 
    #locate the require number the loop will keep iteartaing untill we reach the start
    # become greater than the end
    start=0
    end = len(arr)-1
    mid=0
    while start<=end:
        # in each iteration the start will increase by one and the end will decrease by one
        mid=start+end
        if arr[mid]<n:
            start=mid+1
        elif arr[mid] >n:
            end=mid-1

        else:
          return mid  
          # if the number is not in the list  
    return -1