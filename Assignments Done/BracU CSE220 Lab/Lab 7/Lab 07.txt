#Task 01
class KeyIndex:
    def __init__(self,tmp):
        self.tmp, self.Nlist = tmp, None
        A1 =[]
        present = True
        lenA1 = len(tmp)
        for i in range(lenA1):
            A1 += [tmp[i]]
        for j in range(lenA1):
            if A1[j]<0:
                present=False
        if present is False:
            low = A1[0]
            for i in range(1,lenA1):
                if low > A1[i]:
                    low =A1[i]
            low *= -1
            for j in range(lenA1):
                A1[j]  +=  low
        max = A1[0]
        for i in range(1,lenA1):
            if A1[i] > max:
                max = A1[i]
        self.Nlist =[0]*(max+ 1)
        for i in range(lenA1):
            self.Nlist[A1[i]]= self.Nlist[A1[i]]+1

    def search(self,data):
        self.data = data
        for i in range(len(self.tmp)):
            if self.tmp[i] < 0:
                low = self.tmp[0]
                for j in range(1,len(self.tmp)):
                    if self.tmp[j] < low:
                        low = self.tmp[j]
                low *= -1
                data +=  low
        for i in range(len(self.Nlist)):
            if data > len(self.Nlist):
                print("False")
                break
            elif data ==i:
                if self.Nlist[i]== 0:
                    print("False")
                else:
                    print("True")

    def sort(self):
        cnt = 0
        for i in range(len(self.tmp)):
            if self.tmp[i] <= 0:
                low = self.tmp[0]
                for i in range(1,len(self.tmp)):
                    if low >self.tmp[i]:
                        low = self.tmp[i]
                low *= -1
            elif self.tmp[i] > 0:
                cnt +=  1
            else:
                pass
        if len(self.tmp)>0:
            n = 0
            while n!= len(self.Nlist):
                if self.Nlist[n]!= 0:
                    print((n-low), end=" ")
                    self.Nlist[n]=self.Nlist[n]-1
                n += 1
        else:
            pass


#Task 02
def Htable(A):
    Htable=[0]*9
    lenA = len(A)
    for i in range(lenA):
        con, sum = 0, 0
        for j in A[i]:
            if j in "AEIOUaeiou":
                pass
            elif j>="A" and j<="Z" and j not in "AEIOUaeiou":
                con += 1
            elif int(j) in (0,1,2,3,4,5,6,7,8,9):
                sum += int(j)
            else:
                pass
        y = ( (con * 24) + sum) % 9
        while Htable[y]!= 0:
            y =(y+1) % len(Htable)
        Htable[y] = A[i]
        while Htable[y]==0:
            Htable[y] = A[i]
    print(Htable)

if __name__ == '__main__':

    # T1 start
    list = [1, 3, 2, 4, 6, -5, 0]
    n = KeyIndex(list)
    print("Key Index Search: ")
    n.search(7)
    print("Key Index sorted Array: ")
    n.sort()
    # T1 end

    # T2 Start
    String = ['ST1E89B8A32', 'ST1E89B8A32', 'CB89894', 'ST1E89B8A32']
    print("\nHashing : ")
    Htable(String)
    # T2 End