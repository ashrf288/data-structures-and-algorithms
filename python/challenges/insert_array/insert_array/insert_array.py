
import math
def array_insert_shift(arr,value):
# calculate array length
       # find the middle index in which we will insert the value
    the_middle_index= math.ceil(len(arr)/2)
    newArr=[]
    for i in range(0,len(arr)+1):
       if i==len(arr):
           break
       if i==the_middle_index:
          newArr+=[value]
       newArr+=[arr[i]]  
    return newArr




