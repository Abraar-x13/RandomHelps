#TASK03

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
        
    def bubbleSort(self): 
        
        head1 = self.head
        while (head1.next != None):
            head2 = self.head
            while True:
                if (head2.next == None): 
                    break
                if (head2.element > head2.next.element): 
                    temp = head2.element
                    head2.element = head2.next.element
                    head2.next.element = temp
                head2 = head2.next 
            head1 = head1.next 



#======================= TESTER CODE =======================
list01 = [64, 34, 25, 12, 22, 11, 2] 
list1 = MyList(list01)
list1.bubbleSort()
list1.showList()
