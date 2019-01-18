from grasp import save
import getopt,sys,os
from enuminfo import flowto
def revArgs():
     try:
         opts, args = getopt.getopt(sys.argv[1:], "s:e:n:p:h",["help","type=", "start=","end=","name="])
     except Exception as ex:
         print(ex.args)
         print("the args format:  --start=20180101 --end=20180102 --name=xxxx --type=in/out")
         os._exit(0)
     start=end=name=flowtype=''
     for opt,value in opts :
        if opt in ('-s','--start'):
            start=value
        if opt in ('-e','--end'):
            end=value
        elif opt in ('-n','--name'):
            name=value
        elif opt in ('-p','--type'):
            flowtype=value
     if start=='' or end=='' or name=='' or  flowtype=='':
         print('start ,end,flowtype and name is not empty')
         print("the args format:  --start=20180101 --end=20180102 --name=xxxx  --type==in/out")
         os._exit(0)
     return  start,end,name,flowtype


if __name__ == "__main__":
    start,end,name,flowtype=revArgs()
    if flowtype=='in':
        flowtype=flowto.inflow
    else:
        flowtype=flowto.flowout
    print(start,end ,name ,flowtype )
    save(start,end,name,flowtype)





