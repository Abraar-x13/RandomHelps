#TASK04

#====================== NODE CLASS ========================
class Node:
    def __init__ (self, element = None, next = None):
        self.element = element
        self.next = next
    
    def printNode (self):
        print (self.element, "-", self.next)
        
#==================== LINKED LIST CLASS ========================
class MyList:
    
    def __init__ (self, source = None):
        self.head = None
        tail = None 
          
        count = 0
        while (count < len(source)):            
            n = Node (source[count], None)
            
            if (self.head == None):
                self.head = n
                tail = n                    
            else:
                tail.next = n
                tail = n
                
            count += 1
            
    def showList (self):
        n = self.head
        if (n == None):
            print ("Empty List")  
        while (n != None):
            n.printNode()
            n = n.next
        
    
    def selectionSort(self): 
        
        head1 = self.head 
        while (head1.next != None): 
            minimum = head1 
            head2 = head1.next
            while (head2 != None): 
                if (minimum.element > head2.element): 
                    minimum = head2 
                head2 = head2.next
            temp = head1.element 
            head1.element = minimum.element 
            minimum.element = temp 
            head1 = head1.next
            
#======================= TESTER CODE =======================
list01 = [64, 34, 25, 12, 22, 11, 2] 
list1 = MyList(list01)
list1.selectionSort()
list1.showList()
