import os
infilename=input("What is the name of the file? ")
outfilename=(infilename.replace(".txt","-out.txt"))
if os.path.exists(infilename)==0:
    print("cannot find the input file")
elif os.path.exists(infilename)==1:
    print("input file is found")
    infile=open(infilename,"r")
    outfile=open(outfilename,"w+")
    


    for x in infile:
        outfile.write(x.replace("Electrical Engineering","1").replace("Computer Engineering","2").replace("Mechanical Engineering","3").replace("Civil Engineering","4").replace(";","").replace("Physics","0").replace("Mathematics","0").replace("Business","0").replace("Law","0"))
           
    infile.close()
    outfile.close()
    infile=open(infilename,"r")
    outfile=open(outfilename,"a")
    data=infile.read()
    list1=["The number of Electrical Engineering students: ",str(data.count("Electrical Engineering"))]
    list2=["The number of Computer Engineering students: ",str(data.count("Computer Engineering"))]
    list3=["The number of Mechanical Engineering students: ",str(data.count("Mechanical Engineering"))]
    list4=["The number of Civil Engineering students: ",str(data.count("Civil Engineering"))]
    for i in list1:
        outfile.write(i)
    outfile.write("\n")
    for j in list2:
        outfile.write(j)
    outfile.write("\n")
    for k in list3:
        outfile.write(k)
    outfile.write("\n")
    for l in list4:
        outfile.write(l)
    infile.close()   
    outfile.close()
