from grasp import save
import getopt,sys,os
def revArgs():
     try:
         opts, args = getopt.getopt(sys.argv[1:], "s:e:n:h",["help","start=","end=","name="])
     except Exception as ex:
         print(ex.args)
         print("the args format:  --start=20180101 --end=20180102 --name=xxxx")
         os._exit(0)
     start=end=name=''
     for opt,value in opts :
        if opt in ('-s','--start'):
            start=value
        if opt in ('-e','--end'):
            end=value
        elif opt in ('-n','--name'):
            name=value
     if start=='' or end=='' or name=='':
         print('start ,end and name is not empty')
         print("the args format:  --start=20180101 --end=20180102 --name=xxxx")
         os._exit(0)
     return  start,end,name


if __name__ == "__main__":
    start,end,name=revArgs()
    save(start,end,name)





