#TASK02

#======================= FUNCTION CODE =====================
def insertionSortRecursive(source, length):
    
    if length <= 1:
        return 1
    
    insertionSortRecursive(source, length - 1)
    last = source[length - 1]
    count = length - 2
    maxLocation (source, count, last)

def maxLocation (source, count, last): 
    if (count >= 0 and source[count] > last):
        source[count + 1] = source[count]
        maxLocation (source, count - 1, last)
    else:
        source[count + 1] = last

def print_array (source, count = 0):
    if (count == len(source)):
        return 1
    else:
        print (source[count], end = " ")
        print_array(source, count + 1)
        
#======================= TESTER CODE =======================
source = [12,11,13,5,6]
insertionSortRecursive(source, len(source))
print_array(source)
