#TASK07

#====================== NODE CLASS ========================
source = list()

def CalcFib(num):
    source.insert(0,1)
    source.insert(1,1)
    for count in range(2,num):
        source.insert(count, source[count - 1] + source[count - 2])
    print (source[-1])

#======================= TESTER CODE =======================
CalcFib(46)
