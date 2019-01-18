from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker,join,scoped_session
from DBconfig import GetPathDB_Mysql
from sqlalchemy import and_,text,desc
from models import region ,result


# 初始化数据库连接:
dbpath=GetPathDB_Mysql()


engine = create_engine(dbpath)

session_factory=sessionmaker(bind=engine, autoflush=True)

#thread-local session

db_Session=scoped_session(session_factory)


#region
def find_region(session,sqlwhere=''):
    result=[]
    if sqlwhere == '':
        result = session.query(region).all()
    else:
        result = session.query(region).filter(text(sqlwhere)).all()
    return result

def get_citycode(session,name):
    if '恩施州' == name:
        return '422800'
    if '黔东南' == name:
        return '522600'
    if '昌江' == name:
        return '469026'
    if '大理' == name:
        return '532900'
    if '红河' == name:
        return '532500'
    if '楚雄' == name:
        return '532300'
    if '台湾' == name:
        return '710000'
    if '神农架' == name:
        return '429021'
    if '湘西' == name:
        return '433100'
    if '锡盟' == name:
        return '152500'
    if '西双版纳' == name:
        return '532800'
    if '黔西南' == name:
        return '522300'
    if '文山' == name:
        return '532600'
    if '黔南' == name:
        return '522700'
    if '凉山' == name:
        return '513400'
    if '澄迈县' == name:
        return '469023'
    if '甘南' == name:
        return '623000'
    r=find_region(session,r"name='%s市'"%(name))
    if len(r)>0:
        return r[0].code 
    else:
        return None
def isexist(session,date,dep_citycode,des_citycode):
    r=find_result(session,r"date='%s' and dep_citycode='%s' and des_citycode='%s'"%(date,dep_citycode,des_citycode))

    if len(r) > 0:
        return True
    else:
        return False
def find_result(session,sqlwhere=''):
    data=[]
    if sqlwhere == '':
        data = session.query(result).all()
    else:
        data = session.query(result).filter(text(sqlwhere)).all()
    return data

def add_result(session,result):
    session.add(result)

##r=find_region(session,r"name='黄石市'")
#rt=result()
#rt.date='20180103'
#rt.dep_citycode='420100'
#rt.departure='武汉市'
#rt.des_citycode='xxx'
#rt.destination='xx'
#rt.total=24
#rt.heatvalue=(rt.total/100)**0.5
#rt.bus_persontime=4343
#rt.bus_proportion=0.35
#rt.train_persontime=343
#rt.train_proportion=0.33
#rt.airplane_persontime=343
#rt.airplane_proportion=0.55
#add_result(session,rt)
#session.commit()
#session.close()
#db_Session.remove()















