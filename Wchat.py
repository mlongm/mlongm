import itchat
import xlwt

#t = str.maketrans('','','\'')
dx = {"Uin": 0,"UserName":'',"NickName":'',"HeadImgUrl":'',"ContactFlag":'',"MemberCount":'',"MemberList":'',"RemarkName":'',"HideInputBarFlag":0,"Sex":0,"Signature":'',"VerifyFlag": 0,"OwnerUin": 0,"StarFriend":0,"AppAccountFlag": 0,"Statues": 0,"AttrStatus": 119911,"Province":'',"City":'',"Alias":'', "SnsFlag":0,"UniFriend": 0,"DisplayName":"","ChatRoomId": 0,"KeyWord":'',"EncryChatRoomId":''}
FriendList = []
keys = []
sALL = ' '

def ADDdict(keys):
    #用来筛选字典项
    jian = keys[0].replace('\'','')
    #print(jian)
    zhi = keys[1].replace('\'','')
    #print(zhi)
    #符合条件的项返回True,反之返回False
    if jian in dx:
        return True
    else:
        return False

def EDITstr(strs):
    #清洗数据，重点是去掉引号内的所有逗号。谁说我们需要正则表达式的？
    x = []
    a = ''
    a = strs.replace(' ','')
    #strs = a.replace('<','《')
    #a = strs.replace('>','》')
    for i in range(len(a)):
        x.append(a[i])
    for i in range(len(x)):
        if i > 0 and x[i] == ',':
            if not(x[i-1] == '\'' or x[i+1] == '\''):
                print(str(i) + '   ' + x[i])
                x[i] = ' & '
    a = ''.join(x)
    return a

def GetData(fd):
#获得微信好友信息列表，并返回之。
    name = []
    user = str(fd)
    user = user[9:-3]
    Auser = user.split("}>, <User: {")
    print(len(Auser))
    #提取信息到NAME[]
    for i in range(len(Auser)):
        #对好友信息格式化，去逗号等操作。
        sALL = EDITstr(Auser[i])
        #将好友信息逐项分割。
        dic = sALL.split(",")
        di = {}
        #将信息项分为键和值，生成keys
        for ii in range(len(dic)):
            keys = dic[ii].split(":")
            if ADDdict(keys):
                di[keys[0]] = keys[1]
        
        name.append(di)
        print(len(Auser))        
    return name   

def DataSave(datas):
    wb = xlwt.Workbook(encoding='utf8')
    ws = wb.add_sheet('sheet1')
    y = 0
    lists = []
    for i in datas[0].keys():
        ws.write(0,y,i)
        lists.append(i)
        y += 1
    y = 0
    try:
        for r in range(0,len(datas)):
            d = {}
            cells = ""
            for c in range(len(datas[0])):
                d = datas[r]
                cells = lists[c]
                ws.write(r+1,c,d[cells])
                y += 1
            y = 0
        wb.save('FriendWY.xls')
    except:
        print("程序错误，文件信息未能写入。")

#main()
itchat.auto_login()
fd = itchat.get_friends(update=True)
FriendList = GetData(fd)
DataSave(FriendList)