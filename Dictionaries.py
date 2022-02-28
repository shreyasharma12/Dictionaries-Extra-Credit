def main(): 

    outfile = open("book of John text.txt",'r')

    certainWords = outfile.read().split()

    John = {}

    for i in range(len(certainWords)):
        John[certainWords[i]] = 0

    for i in range(len(certainWords)):
        John[certainWords[i]] += 1



    print("Father:",John['Father'])
    print("God:",John['God'])
    print("Christ:",John['Christ'])
    print("Spirit",John['Spirit'])
    print("spirit:",John['spirit'])
    print("life:",John['life'])
    print("man:",John['man'])

    outfile.close()

main()