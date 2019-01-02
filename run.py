from get_webpage import requestHelper
from webpage_parser import parseHelper
import getopt,sys,os
def revArgs():
     try:
         opts, args = getopt.getopt(sys.argv[1:], "d:c:h",["help","date=","code="])
     except Exception as ex:
         print(ex.args)
         print("the args format:  --date=20180101 --code=xxxx")
         os._exit(0)
     date=code=''
     for opt,value in opts :
        if opt in ('-d','--date'):
             date=value
        elif opt in ('-c','--code'):
            code=value
     return  date,code


if __name__ == "__main__":
    date,code=revArgs()
    rqt=requestHelper(date,code)
    webparser=parseHelper(rqt)
    data_dict=webparser.cleandata()
    print(data_dict)
