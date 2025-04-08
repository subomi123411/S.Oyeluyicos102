def printinfo( arg1, *vartuplpe):
    #Test function
    print("Output is: ")
    print(arg1)
    for var in vartuplpe:
        print(var)
    return
printinfo( 10 )
printinfo( 70, 60, 50 )