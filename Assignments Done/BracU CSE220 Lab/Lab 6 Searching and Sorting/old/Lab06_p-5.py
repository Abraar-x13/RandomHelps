#TASK06

#======================= FUNCTION CODE =====================
def binary_search(source, start, end, value): 
  
    if end >= start: 
        mid = int((start + end) / 2)
  
        if source[mid] == value: 
            print ("Found")

        elif source[mid] > value: 
            return binary_search(source, start, mid - 1, value) 
  
        else: 
            return binary_search(source, mid + 1, end, value) 
  
    else: 
        print ("Not Found")

#======================= TESTER CODE =======================
source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binary_search (source, 0, len(source) - 1, 0)
