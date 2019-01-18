from datetime import datetime,timedelta
from models import result,region
from DataAccess import *
from enuminfo import flowto
import os
import time
def audo_add(strdate,num):
    strdate='%s-%s-%s'%(strdate[0:4],strdate[4:6],strdate[6:8])
    curtime = datetime.strptime(strdate,'%Y-%m-%d')
    endtime=curtime+timedelta(days=num)
    return str(endtime.strftime('%Y%m%d'))


def data2result(curdate,curname,data_list,flowto):
    data=[]
    flag=True
    for record in data_list:
        rt=result()
        session=db_Session()
        try:
            if flowto==flowto.inflow:
                cur_dep_code=get_citycode(session,record[0])
                cur_des_code=get_citycode(session,curname)
                rt.departure=record[0]
                rt.destination=curname
                if not  cur_dep_code:
                    raise Exception('departure:%s is not exist!'%record[0])
                if not cur_des_code:
                    raise Exception('destination:%s, is not exist!'%curname)
            else:
                cur_dep_code=get_citycode(session,curname)
                cur_des_code=get_citycode(session,record[0])
                rt.departure=curname
                rt.destination=record[0]
                if not  cur_dep_code:
                    raise Exception('departure:%s is not exist!'%curname)
                if not cur_des_code:
                    raise Exception('destination:%s, is not exist!'%record[0])
            if isexist(session,curdate,cur_dep_code,cur_des_code):
                continue
            rt.date=curdate
            rt.dep_citycode=cur_dep_code
            rt.des_citycode=cur_des_code
            rt.total=record[1]
            rt.heatvalue=(rt.total/100)**0.5
            rt.bus_persontime=round(rt.total*record[2])
            rt.bus_proportion=record[2]
            rt.train_persontime=round(rt.total*record[3])
            rt.train_proportion=record[3]
            rt.airplane_persontime=round(rt.total*record[4])
            rt.airplane_proportion=record[4]
            data.append(rt)
        except Exception as e:
            flag=False
            print(e.args)       
            print('curdate:%s,departure:%s'%(curdate,curname))
        finally:
            session.close()
            db_Session.remove()
            if not  flag:
                os._exit(0)
    return data
            
