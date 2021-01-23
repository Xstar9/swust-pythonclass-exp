def GetData(name):
    text = ""
    datalist = []
    with open(name,"r",encoding="utf-8") as file:
        text = file.readline().replace("，",",").replace("【","[").replace("】","]")
        datalist = eval(text)
        # print(datalist)
        file.close()
        return  datalist
# GetData("data.txt")
def UnZipData (data):
    data = list(data)
    datalist = []
    for i in range(0,len(data),2):
        dat = []
        dat.append(data[i])
        dat.append(data[i+1])
        datalist.append(dat)
    # print(datalist)
    return  datalist
# UnZipData (GetData("data.txt"))

def SaveData(name,data):
    datalist = []
    for item in data:
        for j in range(0,int(item[1])):
            datalist.append(item[0])
    # print(len(datalist))
    print(datalist)
    datalist = [ str(i) for i in datalist]
    print(datalist)
    text = ",".join(datalist)
    # print(text, type(text))
    with open(name,"a+",encoding="utf-8") as file:
        file.write("\ntotal:"+str(len(datalist)))
        file.write("\n["+text+"]")
        file.close()

SaveData("data.txt",UnZipData (GetData("data.txt")))