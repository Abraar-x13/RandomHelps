#TASK01

#======================= FUNCTION CODE =====================
def minLocation(array, count, count2): 
    if count == count2: 
        return count

    minimum = minLocation(array, count + 1, count2) 
      
    if (array[count] < array[minimum]):
        return count
    else:
        return minimum
      
def recursion_SelectionSort(array, length, index = 0): 
    if index == length: 
        return -1

    minimum = minLocation(array, index, length - 1) 
    if minimum != index: 
        array[minimum], array[index] = array[index], array[minimum] 
    
    recursion_SelectionSort(array, length, index + 1) 

def print_array (array, count = 0):
    if (count == len(array)):
        return 1
    else:
        print (array[count], end = " ")
        print_array(array, count + 1)
    
#======================= TESTER CODE =======================
source = [3, 1, 5, 2, 7, 0] 
recursion_SelectionSort(source, len(source)) 
print_array(source)
