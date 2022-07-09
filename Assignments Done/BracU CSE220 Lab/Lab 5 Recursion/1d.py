# QUESTION: Given base and n that are both 1 or more,
# compute recursivelym(no loops) the value of base
# to the n power, so powerN(3, 2) is 9 (3 squared).

def powerN(base, power):
    if power==0:
        return 1
    return base*powerN(base, power-1)

if __name__ == '__main__':
    nBase = int(input("Enter Base: "))
    nPow = int(input("Enter Power: "))
    print(f"The result : {powerN(nBase, nPow)} ")
    # print(powerN(3, 1))
    # print(powerN(3, 2))
    # print(powerN(3, 3))