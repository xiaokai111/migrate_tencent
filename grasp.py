from get_webpage import requestHelper
from webpage_parser import parseHelper
import getopt,sys,os
from funchelper import audo_add,data2result
from DataAccess import *



def save(start_date,end_date,departure):
    curdate=start_date
    deadline=int(end_date)
    flag=True
    while (int(curdate)<=deadline):
        print('curdate:%s,departure:%s'%(curdate,departure))
        session=db_Session()
        code=get_citycode(session,departure)
        if not code:
            raise Exception('departure:%s  is not exist.'%departure)
        rqt=requestHelper(curdate,'%s16'%code)
        webparser=parseHelper(rqt)
        data_list=webparser.cleandata()
        print(data_list)          
        data=data2result(curdate,departure,data_list)
        try:
            for  v in data:
                add_result(session,v)
            session.commit()
        except Exception as e:
            flag=False
            print(e.args)
            print('curdate:%s,departure:%s'%(curdate,departure))
        finally:
            session.close()
            db_Session.remove()
            if not flag:
                os._exit(0)
        curdate=audo_add(curdate,1)
        
       

 
