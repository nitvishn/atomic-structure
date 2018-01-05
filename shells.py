def getConfig(protonNumber):
    """

    :param protonNumber: the number of protons in the atom.
    :return L: a list of the number of protons in each shell.
    """
    n=protonNumber
    k=1
    L=[]
    while(True):
        maxNumElectrons=2*(k**2)
        if(maxNumElectrons<n):
            L.append(maxNumElectrons)
            n-=maxNumElectrons
        elif(n>8):
            L.append(8)
            n-=8
        else:
            L.append(n)
            return L
        k+=1

print(getConfig(int(input("Proton number: "))))