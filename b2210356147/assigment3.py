import os,sys
current_dir_path=os.getcwd()
commands=[]
if len(sys.argv)>1:
    x=sys.argv[1]
    reading_file_name = x
else:
    reading_file_name = "input.txt"
reading_file_path = os.path.join(current_dir_path, reading_file_name)
with open(reading_file_path, "r") as i:
        count = 0
        while True:
            count += 1
            line = i.readline()
            if not line:
                break
            commands.append(line)
        i.close()
output=[]
listseattable=[]
listcategory=[]
listcategoryarea=[]
def create():
    tempseattable=[]
    found=""
    strcategory=data[0]
    strcategoryarea=data[1]
    listtempseat=strcategoryarea.split("x")
    number1=int(listtempseat[0])
    number2=int(listtempseat[1])
    total=number1*number2
    if number1>26:
        output.append("Warning: Cannot create the category {} as it has too much rows to designate with letters.\n".format(strcategory))
    if number2>99:
        output.append("Warning:Cannot create the category {} as it has too much columns to desinate with utmost two digit numbers.\n".format(strcategory))
    else:
        for i in range(len(listcategory)):
            if strcategory in listcategory[i]:
                found=True
                break
            else:
                found=False
                continue
        if found is True:
            output.append("Warning: Cannot create the category for the second time. The stadium has already {}.\n".format(strcategory))
        else:
            for i in range(number1):
                for j in range(number2):
                    tempseattable.append("X")
            listseattable.append(tempseattable)
            listcategory.append(strcategory)
            listcategoryarea.append(strcategoryarea)
            output.append("The category {} having {} seats has been created.\n".format(strcategory,total))
listseat=[]
alphabet={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
listalphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
stralphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def sell():
    strname=data[0]
    data.pop(0)
    strtickettype=data[0]
    data.pop(0)
    strcategory=data[0]
    data.pop(0)
    for i in range(len(listcategory)):
        if strcategory in listcategory[i]:
            found=True
            break
        else:
            found=False
            continue
    if found is False:
        output.append("Warning: Cannot sell ticket as stated category {} does not exist.\n".format(strcategory))
    else:
        a=listcategory.index(strcategory)
        strcategoryarea=""
        for i in range(len(listcategoryarea[a])):
            strcategoryarea+=listcategoryarea[a][i]
        listtempseat=strcategoryarea.split("x")
        number1=int(listtempseat[0])
        number2=int(listtempseat[1])
        tempdata=[]
        strtempdata=""
        templetter=""
        tempnumber=0
        tempnumber0=0
        templetterlocation=0
        for i in range(len(data)):
            for j in range(len(data[i])):
                tempdata+=data[i][j]
        for i in range(len(tempdata)):
            if tempdata[i]in stralphabet:
                templetter+=tempdata[i]
                strtempdata+="#"
            else:
                strtempdata+=tempdata[i]
        tempdata=strtempdata.split("#")
        tempdata.pop(0)
        tempstr=""
        for j in range(len(tempdata)):
            for k in range(len(templetter)):
                if len(tempdata[j])==1:
                    tempstr=tempdata[j][0]
                    tempnumber=int(tempstr)
                if len(tempdata[j])==2:
                    inttempdata1=tempdata[j][0]
                    inttempdata2=tempdata[j][1]
                    tempstr=inttempdata1+inttempdata2
                    tempnumber=int(tempstr)
                if len(tempdata[j])==3:
                    tempnumber0=int(tempdata[j][0])
                    tempnumber=int(tempdata[j][2])
                if len(tempdata[j])==4:
                    tempnumber0=int(tempdata[j][0])
                    inttempdata1=tempdata[j][2]
                    inttempdata2=tempdata[j][3]
                    tempnumber=int(inttempdata1+inttempdata2)
                if len(tempdata[j])==5:
                    inttempdata1=tempdata[j][0]
                    inttempdata2=tempdata[j][1]
                    inttempdata3=tempdata[j][3]
                    inttempdata4=tempdata[j][4]
                    tempnumber0=int(inttempdata1+inttempdata2)
                    tempnumber=int(inttempdata3+inttempdata4)
                    templetterlocation=int(alphabet.get(templetter[k]))
        if templetterlocation>number1:
            output.append("Error: The category {} has less lines than the specified index!\n".format(strcategory))
        if tempnumber>number2:
            output.append("Error: The category {} has less columns than the specified index!\n".format(strcategory))
        else:
            for j in range(len(tempdata)):
                for k in range(len(templetter)):
                    strtempseat=""
                    stroutputseat=""
                    tempseat=[]
                    tempoutputseat=[]
                    if len(tempdata[j])<3:
                        strtempseat+=strcategory+"#"+templetter[k]+tempstr+"#"+","
                        stroutputseat+=templetter[k]+tempstr+","
                    if 3<=len(tempdata[j])<=5:
                        for i in range(tempnumber0,tempnumber+1):
                            strtempseat+=strcategory+"#"+templetter[k]+str(i)+"#"+","
                            stroutputseat+=templetter[k]+str(i)+","
                    tempseat=strtempseat.split(",")
                    tempseat.remove("")
                    tempoutputseat=stroutputseat.split(",")
                    tempoutputseat.remove("")
        for i in range(len(tempseat)):
            if tempseat[i] in listseat:
                found=True
                break
            else:
                found=False
                continue
        if found is True:
            output.append("Error: The seat(s) {} cannot be sold to {} since some or all have been sold.\n".format(tempoutputseat,strname))
        else:
            listseat.extend(tempseat)
            output.append("Success: {} has bought {} at {}.\n".format(strname,tempoutputseat,strcategory))
        
            for j in range(len(tempdata)):
                for k in range(len(templetter)):
                    if len(tempdata[j])<3:
                        if strtickettype=="student":
                            listseattable[a].pop((int(alphabet.get(templetter[k],1))-1)*number1+tempnumber-1)
                            listseattable[a].insert((int(alphabet.get(templetter[k],1))-1)*number1+tempnumber-1,'S')
                        if strtickettype=="full":
                            listseattable[a].pop((int(alphabet.get(templetter[k],1))-1)*number1+tempnumber-1)
                            listseattable[a].insert((int(alphabet.get(templetter[k],1))-1)*number1+tempnumber-1,'F')
                        if strtickettype=="season":
                            listseattable[a].pop((int(alphabet.get(templetter[k],1))-1)*number1+tempnumber-1)
                            listseattable[a].insert((int(alphabet.get(templetter[k],1))-1)*number1+tempnumber-1,'T')
                    if 3<=len(tempdata[j])<=5:
                        if strtickettype=="student":
                            for i in range(tempnumber0,tempnumber+1):
                                listseattable[a].pop((int(alphabet.get(templetter[k],1))-1)*number1+i-1)
                                listseattable[a].insert((int(alphabet.get(templetter[k],1))-1)*number1+i-1,'S')
                        if strtickettype=="full":
                            for i in range(tempnumber0,tempnumber+1):
                                listseattable[a].pop((int(alphabet.get(templetter[k],1))-1)*number1+i-1)
                                listseattable[a].insert((int(alphabet.get(templetter[k],1))-1)*number1+i-1,'F')
                        if strtickettype=="season":
                            for i in range(tempnumber0,tempnumber+1):
                                listseattable[a].pop((int(alphabet.get(templetter[k],1))-1)*number1+i-1)
                                listseattable[a].insert((int(alphabet.get(templetter[k],1))-1)*number1+i-1,'T')
def cancel():
    strcategory=data[0]
    data.pop(0)
    for i in range(len(listcategory)):
        if strcategory in listcategory[i]:
            found=True
            break
        else:
            found=False
            continue
    if found is False:
        output.append("Warning: Cannot cancel seats as stated category {} does not exist.\n".format(strcategory))
    else:
        a=listcategory.index(strcategory)
        strcategoryarea=""
        for i in range(len(listcategoryarea[a])):
            strcategoryarea+=listcategoryarea[a][i]
        listtempseat=strcategoryarea.split("x")
        number1=int(listtempseat[0])
        number2=int(listtempseat[1])
        tempdata=[]
        for i in range(len(data)):
            templetter=data[i][0]
            for j in range(len(data[i])):
                tempdata+=list(data[i][j])
        tempdata.pop(0)
        if len(tempdata)==1:
            tempstr=tempdata[0]
            tempnumber=int(tempstr)
        if len(tempdata)==2:
            inttempdata1=tempdata[0]
            inttempdata2=tempdata[1]
            tempstr=inttempdata1+inttempdata2
            tempnumber=int(tempstr)
        if len(tempdata)==3:
            tempnumber0=int(tempdata[0])
            tempnumber=int(tempdata[2])
        if len(tempdata)==4:
            tempnumber0=int(tempdata[0])
            inttempdata1=tempdata[2]
            inttempdata2=tempdata[3]
            tempnumber=int(inttempdata1+inttempdata2)
        if len(tempdata)==5:

            inttempdata1=tempdata[0]
            inttempdata2=tempdata[1]
            inttempdata3=tempdata[3]
            inttempdata4=tempdata[4]
            tempnumber0=int(inttempdata1+inttempdata2)
            tempnumber=int(inttempdata3+inttempdata4)
        templetterlocation=int(alphabet.get(templetter))
        if templetterlocation>number1:
            output.append("Error: The category {} has less lines than the specified index!\n".format(strcategory))
        if tempnumber>number2:
            output.append("Error: The category {} has less columns than the specified index!\n".format(strcategory))
        else:
            strtempseat=""
            stroutputseat=""
            tempseat=[]
            tempoutputseat=[]
            if len(tempdata)<3:
                strtempseat+=strcategory+"#"+templetter+tempstr+"#"+","
                stroutputseat+=templetter+tempstr+","
            if 3<=len(tempdata)<=5:
                for i in range(tempnumber0,tempnumber+1):
                    strtempseat+=strcategory+"#"+templetter+str(i)+"#"+","
                    stroutputseat+=templetter+str(i)+","
            tempseat=strtempseat.split(",")
            tempseat.remove("")
            tempoutputseat=stroutputseat.split(",")
            tempoutputseat.remove("")
            for i in range(len(tempseat)):
                if tempseat[i] in listseat:
                    found=True
                    break
                else:
                    found=False
                    continue
            if found is False:
                output.append("Error: The seat(s) {} at {} have already been free! Nothing to cancel.\n".format(tempoutputseat,strcategory))
            else:
                output.append("Success: The seat(s) {} at {} have been cancelled and now ready to sell again.\n".format(tempoutputseat,strcategory))
                if len(tempdata)<3:
                    listseattable[a].pop((int(alphabet.get(templetter))-1)*number1+tempnumber-1)
                    listseattable[a].insert((int(alphabet.get(templetter))-1)*number1+tempnumber-1,'X')
                if 3<=len(tempdata)<=5:
                    listseattable[a].pop((int(alphabet.get(templetter))-1)*number1+i-1)
                    listseattable[a].insert((int(alphabet.get(templetter))-1)*number1+i-1,'X')
def balance():
    strcategory=data[0]
    for i in range(len(listcategory)):
        if strcategory in listcategory[i]:
            found=True
            break
        else:
            found=False
            continue
    if found is False:
        output.append("Warning: Cannot check balance as stated category {} does not exist.\n".format(strcategory))
    else:
        a=listcategory.index(strcategory)
        countstudent=listseattable[a].count("S")
        countfull=listseattable[a].count("F")
        countseason=listseattable[a].count("T")
        revenue=countstudent*10+countfull*20+countseason*250
        output.append("Category report of {}\n".format(strcategory))
        output.append("--------------------------------\n")
        output.append("Sum of students = {}, Sum of full pay = {} Sum of season ticket = {}, and Revenues = ${}\n".format(countstudent,countfull,countseason,revenue))
def show():
    strcategory=data[0]
    for i in range(len(listcategory)):
        if strcategory in listcategory[i]:
            found=True
            break
        else:
            found=False
            continue
    if found is False:
        output.append("Warning: Cannot show category as stated category {} does not exist.\n".format(strcategory))
    else:
        a=listcategory.index(strcategory)
        strcategoryarea=""
        listtempseattable=[]
        strseattable=""
        listshowcategory=[]
        for i in range(len(listcategoryarea[a])):
            strcategoryarea+=listcategoryarea[a][i]
            listtempseat=strcategoryarea.split("x")
        for i in range(len(listseattable[a])):
            listtempseattable+=listseattable[a][i]
        for i in range(2*len(listtempseattable)):
            if listtempseattable[i]=="X":
                listtempseattable.insert(i+1,"\t")
            if listtempseattable[i]=="S":
                listtempseattable.insert(i+1,"\t")
            if listtempseattable[i]=="F":
                listtempseattable.insert(i+1,"\t")
            if listtempseattable[i]=="T":
                listtempseattable.insert(i+1,"\t")
        for i in range(len(listtempseattable)):
            strseattable+=listtempseattable[i]
        number1=int(listtempseat[0])
        number2=int(listtempseat[1])
        tempshowcategory=[(strseattable[i:i+2*number2]) for i in range(0,len(strseattable),2*number2)]
        tempshowcategory.reverse()
        for i in range(number1):
            listshowcategory+=listalphabet[i]
        listshowcategory.reverse()
        output.append("Printing category layout of {}\n\n".format(strcategory))
        for i in range(len(tempshowcategory)):
            output.append("{}\t{}\n\n".format(listshowcategory[i],tempshowcategory[i]))
        output.append("\t")
        for i in range(1,number2+1):
            output.append("{}\t".format(i))
        output.append("\n")
for i in range(len(commands)):
    strstep1=""
    strstep2=""
    for x in commands[i]:
        strstep1+=x
    for x in strstep1.splitlines():
        strstep2+=x
    data=strstep2.split(" ")
    funct=data[0]
    if funct=="CREATECATEGORY":
        data.pop(0)
        create()
    if funct=="SELLTICKET":
        data.pop(0)
        sell()
    if funct=="CANCELTICKET":
        data.pop(0)
        cancel()
    if funct=="BALANCE":
        data.pop(0)
        balance()
    if funct=="SHOWCATEGORY":
        data.pop(0)
        show()
    data.clear
writing_file_name = "output.txt"
writing_file_path = os.path.join(current_dir_path, writing_file_name)
with open(writing_file_path,"w") as o:
    stroutput=""
    for x in output:
        stroutput += x
    o.write(stroutput)
o.close()