#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import calendar,zipfile
import  socket,time
import re,os,sys
from os import system
import subprocess
from datetime import datetime,timedelta
# from mysite.DAL.DBconfig import basedir

_subnet_regex=r'^(254|252|248|240|224|192|128|0)\.0\.0\.0|255\.(254|252|248|240|224|192|128|0)\.0\.0|255\.255\.(254|252|248|240|224|192|128|0)\.0|255\.255\.255\.(254|252|248|240|224|192|128|0)$'
network_filename=r'/etc/NetworkManager/system-connections/Connect_One'

# network_filename=os.path.join('','Connect_One')

__IP_FileName=r'/etc/NetworkManager/system-connections/Connect_One'

def get_mac_address2():
    import uuid
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
    return ('%s:%s:%s:%s:%s:%s' % (mac[0:2],mac[2:4],mac[4:6],mac[6:8],mac[8:10],mac[10:]))

def getMacAddress():
    '''
    @summary: return the MAC address of the computer
    '''
    mac = None
    if sys.platform == "win32":
        for line in os.popen("ipconfig /all"):
            # print line.decode('gbk')
            lineChina = line
            if lineChina.lstrip().startswith("Physical Address"):
                mac = line.split(":")[1].strip().replace("-", ":")
                break
            elif lineChina.lstrip().startswith(u"物理地址"):
                mac = line.split(":")[1].strip().replace("-", ":")
                break
    else:
        for line in os.popen("/sbin/ifconfig"):
            if 'Ether' in line:
                mac = line.split()[4]
                break
    return mac


def getIPAddress():
    '''
    @summary: return the MAC address of the computer
    '''
    import sys
    import os
    ip = None
    if sys.platform == "win32":
        for line in os.popen("ipconfig /all"):
            # print line.decode('gbk')
            # lineChina = line.decode('gbk')
            lineChina=line
            if lineChina.lstrip().startswith("IPv4 Address"):
                ip = line.split(":")[1].strip().replace("-", ":")
                break
            elif lineChina.lstrip().startswith(u"IPv4 地址"):
                ip = line.split(":")[1].strip().replace("-", ":")
                ip = ip.split("(")[0].strip()
                break
    else:
        try:
            csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            csock.connect(('8.8.8.8', 80))
            (addr, port) = csock.getsockname()
            csock.close()
            ip=addr
        except socket.error:
            ip= "127.0.0.1"

    return ip


def getIPAddress2():
    '''
    设置IP
    :param newIP:
    :return:
    '''
    try:
        f = open(network_filename, 'r')
        data=f.readlines()
        print(data)
        f.close()
        for index,item in enumerate(data):
            if 'address1' in item:
                r=re.findall(r'=(.*),',item)
                ip=r[0].split(r'/')[0]
                return ip.strip()
    except Exception as e:
        print(e.args)
        f.close()


def getSubnetMaskAddress(ifname):
    '''
    @summary: return the MAC address of the computer
    '''
    import sys
    import os
    SubnetMask = None

    if sys.platform == "win32":
        for line in os.popen("ipconfig /all"):
            # print line.decode('gbk')
            lineChina = line
            if lineChina.lstrip().startswith("Subnet ask"):
                SubnetMask = line.split(":")[1].strip().replace("-", ":")
                break
            elif lineChina.lstrip().startswith(u"子网掩码 "):
                SubnetMask = line.split(":")[1].strip().replace("-", ":")
                break
    else:
        ipconfig_process = subprocess.Popen(["ifconfig",ifname], stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        mask_str = '0x([0-9a-f]{8})'
        ip_str = '([0-9]{1,3}\.){3}[0-9]{1,3}'
        mask_pattern = re.compile(r'Mask:%s' % ip_str)
        pattern = re.compile(ip_str)
        masklist = []
        for maskaddr in mask_pattern.finditer(str(output)):
            mask = pattern.search(maskaddr.group())
            if mask.group() != '0xff000000' and mask.group() != '255.0.0.0':
                masklist.append(mask.group())
        SubnetMask=masklist[0]
    return SubnetMask

def getDefaultGatewayAddress():
    '''
    @summary: return the MAC address of the computer
    '''
    import sys
    import os
    defaultGateway = None
    if sys.platform == "win32":
        for line in os.popen("ipconfig /all"):
            # print line.decode('gbk')
            lineChina = line
            if lineChina.lstrip().startswith("Default Gateway"):
                defaultGateway = line.split(":")[1].strip().replace("-", ":")
                break
            elif lineChina.lstrip().startswith(u"默认网关"):
                defaultGateway = line.split(":")[1].strip().replace("-", ":")
                break
    else:
        data = os.popen("ip route show | grep 'default'").read()
        pattern = re.compile(r"((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))")
        result=pattern.findall(data)
        defaultGateway=result[0][0]
    return defaultGateway

def getDefaultGatewayAddress2():
    '''
    设置IP
    :param newIP:
    :return:
    '''
    try:
        f = open(network_filename, 'r')
        data=f.readlines()
        print(data)
        f.close()
        for index,item in enumerate(data):
            if 'address1' in item:
                r=re.findall(r',(.*)',item)
                gateway=r[0]
                return gateway.strip()
    except Exception as e:
        print(e.args)
        f.close()

def SetIp(newIP):
    '''
    设置IP
    :param newIP:
    :return:
    '''
    f=open(__IP_FileName,'rb')
    try:
        data=f.readlines()
        f.close()
        for index,item in enumerate(data):
            if 'Address' in item:
                data[index]=('Address=%s/24\r\n'% newIP).encode('utf-8')
                break
        print(data)
        f= open(__IP_FileName,'wb')
        f.writelines(data)
        f.close()
    except Exception as e:
        f.close()

def SetGateway(newGateway):
    '''
    设置新的网关
    :param newGateway:
    :return:
    '''
    f=open(__IP_FileName,'rb')
    print('1')
    try:
        data=f.readlines()
        print(data)
        f.close()
        for index,item in enumerate(data):
            if 'Gateway' in item:
                data[index]=('Gateway=%s\r\n'% newGateway).encode('utf-8')
                print(data)
                break
        print(data)
        f= open(__IP_FileName,'wb')
        f.writelines(data)
        f.close()
    except Exception as e:
        f.close()


def SetGateway2(newGateway):
    '''
    设置新的网关
    :param newGateway:
    :return:
    '''
    f=open(network_filename,'r')
    try:
        data=f.readlines()
        print(data)
        f.close()
        for index,item in enumerate(data):
            if 'address1' in item:
                data[index]=('Gateway=%s\r\n'% newGateway).encode('utf-8')
                print(data)
                break
        print(data)
        f= open(__IP_FileName,'wb')
        f.writelines(data)
        f.close()
    except Exception as e:
        f.close()

def Set_ipANDgatewayANDmask(ip,mask,gateway):
    subnet_decimeal=CountIpOne(mask)

    update_data='address1=%s/%s,%s\n'%(ip,str(subnet_decimeal),gateway)

    try:
        f = open(network_filename, 'r')
        data = f.readlines()
        print("9999999999999999999999999999999999999")
        print(data)
        f.close()
        for index, item in enumerate(data):
            if 'address1' in item:
                data[index] = update_data
                break
        print('##################################################################################')
        print(data)
        write_data=''.join(data)
        print('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
        print(write_data)
        f1 = open(network_filename, 'wb')
        f1.write(write_data.encode('utf-8'))
        f1.close()
    except Exception as e:
        f1.close()


def SetDNS(newDNS):
    '''
    设置新的DNS
    :param newDNS:
    :return:
    '''
    f=open(__IP_FileName,'rb')
    try:
        data=f.readlines()
        f.close()
        for index,item in enumerate(data):
            if 'DNS' in item:
                data[index]=('DNS=%s\r\n'% newDNS).encode('utf-8')
                break
        print(data)
        f= open(__IP_FileName,'wb')
        f.writelines(data)
        f.close()
    except Exception as e:
        f.close()

def CountBinaryOne(num):
    '''
    通知一个十进制数转化成二进制时，包含多少个1
    :param num:
    :return:
    '''
    result=0
    num=int(num)
    while num!=0:
        result+=num%2
        num>>=1
    return result

def CountIpOne(adr_IP):
    '''
    统计IP地址转成二进制时，总共包含多少个1
    :param adr_IP:
    :return:
    '''
    data=adr_IP.split('.')
    result=0
    for v in data:
        result=result+CountBinaryOne(int(v))
    return result

def SetSubNet(newIP,newSubNet):
    '''
        设置子网掩码
        :param newSubNet:新的子网掩码
        :param newIP:新的IP
        :return:
        '''
    f = open(__IP_FileName, 'rb')
    try:
        data = f.readlines()
        f.close()
        subnet_decimeal=CountIpOne(newSubNet)
        for index, item in enumerate(data):
            if 'Address' in item:
                data[index] = ('Address=%s/%s\r\n' % (newIP,subnet_decimeal)).encode('utf-8')
                break
        print(data)
        f = open(__IP_FileName, 'wb')
        f.writelines(data)
        f.close()
    except Exception as e:
        f.close()

def Reboot():
    '''
    重启系统
    :return:
    '''
    system('reboot')


def isLinuxPlatform():
    if 'linux' in sys.platform:
        return True
    else:
        return False

def GetParentPath(curpath, n):
    temp = curpath
    for i in range(n):
        temp = os.path.dirname(temp)
    return temp

def strDateTodigit8bit(strdate):
    '''
    将日期如2018-01-01转化为8位数字字符串
    :param strdate: 如2018-01-15
    :return: ‘20180115’
    '''
    date = datetime.strptime(strdate, '%Y-%m-%d')

    year=date.year

    month='%02d'%date.month

    day='%02d'%date.day


    result='%s%s%s'%(year,month,day )

    return result

def AddDays(start, num):
    '''
    after some days
    :param start:format:'20110101 '
    :param num:
    :return:20110102
    '''
    start = '%s-%s-%s' % (start[0:4], start[4:6], start[6:])
    start = datetime.strptime(start, '%Y-%m-%d')
    result = start + timedelta(days=num)
    result = result.strftime('%Y%m%d')
    return result

def ConvertDate(strData):
    '''

    :param strData: example format: '20171010'
    :return:
    '''
    start = '%s-%s-%s' % (strData[0:4], strData[4:6], strData[6:])
    start = datetime.strptime(start, '%Y-%m-%d')
    return start

def GetOneDayTime(strdate):
    '''
    给出日期，返回改天的时间范围
    :param strdate:‘2018-01-01’
    :return:
    '''
    starttime='%s 00:00:00'%strdate

    endtime='%s 23:59:59'%strdate

    return starttime,endtime

def GetOneDayTime2(strdate):
    '''
    给出日期，返回改天的时间范围
    :param strdate:'20180101'
    :return: ('2018-01-01 00:00:00','2018-01-01 23:59:59')
    '''
    time = '%s-%s-%s' % (strdate[0:4], strdate[4:6], strdate[6:])

    starttime='%s 00:00:00'%time

    endtime='%s 23:59:59'%time

    return starttime,endtime

def GetOneWeekTime(strdate):
    '''
    给出日期，返回这个日期止，前推一个周的时间点
    :param strdate: '2018-01-07'
    :return: ('2018-01-01 00:00:00','2018-01-07 23:59:59')
    '''
    endtime = '%s 23:59:59' % strdate

    strdate_8bit=strDateTodigit8bit(strdate)

    startdate = AddDays(strdate_8bit, -6)

    startdate = '%s-%s-%s' % (startdate[0:4], startdate[4:6], startdate[6:])

    starttime = '%s 00:00:00' % startdate
    return starttime, endtime

def GetOneWeekTime2(strdate):
    '''
    给出日期，返回这个日期止，前推一个周的时间点
    :param strdate: '20180107'
    :return: ('2018-01-01 00:00:00','2018-01-07 23:59:59')
    '''
    enddate = '%s-%s-%s' % (strdate[0:4], strdate[4:6], strdate[6:])
    endtime = '%s 23:59:59' % enddate

    startdate=AddDays(strdate,-6)

    startdate='%s-%s-%s' % (startdate[0:4], startdate[4:6], startdate[6:])

    starttime = '%s 00:00:00' % startdate
    return starttime, endtime

def GetOneMonthTime2(strdate):
    '''
    给出日期，返回这个日期止，前推一个月的时间点
    :param strdate: '20180701'
    :return: ('2018-07-01 00:00:00','2018-07-31 23:59:59')
    '''
    temp=calendar.monthrange(int(strdate[0:4]),int(strdate[4:6]))

    enddate = '%s-%s-%s' % (strdate[0:4], strdate[4:6], str(temp[1]))
    endtime = '%s 23:59:59' % enddate

    startdate='%s-%s-%s' % (strdate[0:4], strdate[4:6], '01')

    starttime = '%s 00:00:00' % startdate
    return starttime, endtime


def GetNextMonthEnd(strdate):
    '''
    根据当前日期得到下月底的日期
    :param strdate: '20180105'
    :return: '20180228'
    '''
    daterange=calendar.monthrange(int(strdate[0:4]),int(strdate[4:6]))

    strdate='%s%s'%(strdate[0:6], daterange[1])

    nextMonth= AddDays(strdate,1)

    nextdaterange = calendar.monthrange(int(nextMonth[0:4]), int(nextMonth[4:6]))

    nextMonth='%s%s'%(nextMonth[0:6], nextdaterange[1])

    return nextMonth


def GetNextMonthStart(strdate):
    '''
    根据当前日期得到下月初的日期
    :param strdate: '20180105'
    :return: '20180228'
    '''
    daterange=calendar.monthrange(int(strdate[0:4]),int(strdate[4:6]))

    strdate='%s%s'%(strdate[0:6], daterange[1])

    nextMonth= AddDays(strdate,1)


    nextMonth='%s%2d'%(nextMonth[0:6],1 )

    return nextMonth


def GetCurMonthEnd(strdate):
    '''
    得到当月月末日期
    :param strdate: ‘20180102’
    :return: ‘2018-01-31’
    '''
    daterange = calendar.monthrange(int(strdate[0:4]), int(strdate[4:6]))

    strdate = '%s%s' % (strdate[0:6], daterange[1])

    return strdate

def GetCurMonthStart(strdate):
    '''
    得到当月月初日期
    :param strdate: ‘20180102’
    :return: ‘2018-01-31’
    '''
    daterange = calendar.monthrange(int(strdate[0:4]), int(strdate[4:6]))

    strdate = '%s%2d' % (strdate[0:6], 1)

    return strdate


# 将制定类型下的一系列参数id和默认id提取出来
def convertRadioFormData(radios):
    radioList = []
    defaultValue = 0
    for radio in radios:
        tempRadio = (str(radio.Id), radio.Name, )
        radioList.append(tempRadio)
        if radio.IsDefault == True:
            defaultValue = str(radio.Id)
    return (radioList, defaultValue)

def GetTimeStamp():
    t=time.time()
    timestamp=int(round(t*10000))
    return timestamp

def hex2Rgb(tmp):
    opt = re.findall(r'(.{2})', tmp)  # 将字符串两两分割
    strs = ""  # 用以存放最后结果
    for i in range(0, len(opt)):  # for循环，遍历分割后的字符串列表
        strs += str(int(opt[i], 16)) + ","  # 将结果拼接成12，12，12格式

    return strs[0:-1]


def rgb2hex(rgbcolor):
  r, g, b =[int(i) for i in rgbcolor.split(',')]

  d=(r << 16) + (g << 8) + b

  d=hex(d)

  return d[2:]


def mkdir(path):
    path = path.strip()
    if isLinuxPlatform():
        path=path.rstrip(r'/')
    else:
        path = path.rstrip("\\")

    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        os.makedirs(path)
        return True,path
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print('%s already existed!'%path)
        return False,path


def GenerateZip(dirpath,zipName):
    '''
    Generate zip file
    :param dirpath: some files what  need to be  compressed
    :param zipName:as zip  name after having generated and is a full filename
    :return:
    '''
    destZip = zipfile.ZipFile(zipName, "w")
    for parent, dirnames, filenames in os.walk(dirpath):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        print('all files:',filenames)
        for filename in filenames:  # 输出文件信息
            if '.zip' in filename:
                continue
            try:
                destZip.write(os.path.join(parent, filename), filename)
            except:
                continue
    destZip.close()
    print ("Zip folder succeed!")

def GetDeviceTime():
    '''
    获取linux系统时间（如2017-08-09T15:50）
    :return:
    '''
    if isLinuxPlatform():
        result = os.popen('date +%Y-%m-%dT%H:%M:%S')
        res = result.read()
        data = res.splitlines()[0]
        data=data.replace('T',' ')
        now = datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
        # delta = timedelta(hours=8)
        # hours = now + delta
        strNow = now.strftime('%Y-%m-%d %H:%M:%S')
        return strNow
    else:
        data='1999-01-01 00:00:00'
    return data




def SetDeviceTime(newTime):
    '''
    设置linux系统时间并同步到硬件时间
    :param newTime: 时间格式2017-01-01 15:22:20
    :return:
    '''
    os.system("date -s '%s' && %s" % (newTime, 'hwclock -w'))
    os.system('sync')


def isrepeat(starttime1,endtime1,starttime2,endtime2):
    '''
    判断两个时间段是否存在交集 max(s1,s2)-min(e1,e2)>0 则无交集
    :param starttime1: '06:00:00'
    :param endtime1:  '08:00:00'
    :param starttime2: '06:30:00'
    :param endtime2:  '07:00:00'
    :return: 如果区间有重复，则返回true 。否则 false
    '''

    temp_s1 = starttime1.split(':')
    temp_s2= starttime2.split(':')
    cur_s1 = int(temp_s1[0]) * 3600 + int(temp_s1[1]) * 60 + int(temp_s1[2])
    cur_s2 = int(temp_s2[0]) * 3600 + int(temp_s2[1]) * 60 + int(temp_s2[2])



    s_list=[]
    s_list.append(cur_s1)
    s_list.append(cur_s2)

    temp_e1 = endtime1.split(':')
    temp_e2 = endtime2.split(':')
    cur_e1 = int(temp_e1[0]) * 3600 + int(temp_e1[1]) * 60 + int(temp_e1[2])
    cur_e2 = int(temp_e2[0]) * 3600 + int(temp_e2[1]) * 60 + int(temp_e2[2])

    e_list=[]
    e_list.append(cur_e1)
    e_list.append(cur_e2)


    max_s=max(s_list)

    min_e=min(e_list)

    if max_s-min_e>=0:
        return False
    else:
        return True


def isrepeat2(timeplanlist):
    '''
    在一系列的时间段中，判断时区是否存在交叉，若是返回True，否则返回False;
    :param timeplanlist: 数据格式举例   [{'starttime':'06:00:00','endtime':'08:00:00'}]
    :return:
    '''
    S=[]
    E=[]
    total=0

    data=[]

    for v in timeplanlist:
        if v['starttime'] == '' or v['endtime'] == '':
            continue
        temp_s = v['starttime'].split(':')
        temp_e = v['endtime'].split(':')
        cur_s = int(temp_s[0]) * 3600 + int(temp_s[1]) * 60 + int(temp_s[2])
        cur_e = int(temp_e[0]) * 3600 + int(temp_e[1]) * 60 + int(temp_e[2])
        if cur_s>=cur_e:
            continue

        data.append(v)

    count=len(data)


    for i,v in enumerate(data):
        j=i+1
        while(j<count):
            if isrepeat(v['starttime'],v['endtime'],data[j]['starttime'],data[j]['endtime']):
                return True
            j=j+1

    return False











