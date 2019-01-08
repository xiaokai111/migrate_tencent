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


#def finduser(session,sqlwhere=''):
#    result=[]
#    if sqlwhere == '':
#        result = session.query(user).all()
#    else:
#        result = session.query(user).filter(text(sqlwhere)).all()
#    return result
#
#
#def UpdateUser_db(session,username,data_dict):
#    session.query(user).filter(user.name == username).update(data_dict)
#
#
#def UpdateUser2_db(session,userid,data_dict):
#    session.query(user).filter(user.id == userid).update(data_dict)
#
#
##endregion
#
#
##region workpos model
#
#
##规则类型
#def GetRuleType(session,sqlwhere=''):
#    result=[]
#    if sqlwhere == '':
#        result = session.query(ruletype).all()
#    else:
#        result = session.query(ruletype).filter(text(sqlwhere)).all()
#    return result
#
#
##获取区域信息
#def GetWorkposDetail(session,sqlwhere=''):
#    result=[]
#    if sqlwhere == '':
#        result = session.query(analysisarea).all()
#    else:
#        result = session.query(analysisarea).filter(text(sqlwhere)).all()
#    return result
#
##获取区域信息及其规则
#def GetAreainfo(session,sqlwhere=''):
#    if sqlwhere == '':
#        result = session.query(alys_ruletype).all()
#    else:
#        result = session.query(alys_ruletype).filter(text(sqlwhere)).all()
#    return result
#
#
#def select_AreaByPage(session,PageIndex,PageSize=10,sqlwhere=''):
#    '''
#       对区域信息进行分页查询
#       :param PageIndex: 页索引值
#       :param PageSize: 每页显示数量
#       :param sqlwhere:筛选条件
#       :return:返回分页数据集和总的记录数
#    '''
#    if sqlwhere != '':
#        total= session.query(analysisarea).order_by(analysisarea.id).filter(text(sqlwhere)).count()
#        data= session.query(analysisarea).order_by(analysisarea.id).filter(text(sqlwhere)).limit(PageSize).offset(PageIndex).all()
#    else:
#        total = session.query(analysisarea).order_by(analysisarea.id).count()
#        data = session.query(analysisarea).order_by(analysisarea.id).limit(PageSize).offset(PageIndex).all()
#    return (total,data)
#
#
#def GetRuleParamBytbname(session,tablename,sqlwhere=''):
#    if not tablename:
#        return None
#    model = eval(tablename)
#    if sqlwhere=='':
#        result = session.query(model).filter(text(sqlwhere)).all()
#    else:
#        result = session.query(model).filter(text(sqlwhere)).all()
#    return result
#
#def UpdateWorkpos_db(session,workposid,data_dict):
#
#    session.query(analysisarea).filter(analysisarea.id == workposid).update(data_dict)
#
#def DelWorkpos_db(session,del_areaids):
#
#    Area_Rulelist=session.query(alys_ruletype).filter(text('analysisareaid in (%s)'%del_areaids)).all()
#
#    if len(Area_Rulelist)<=0:
#        curarealist=session.query(analysisarea).filter(text('id in (%s)'% del_areaids)).all()
#
#        for a in curarealist:
#            session.delete(a)
#    else:
#
#        for v in Area_Rulelist:
#            model = eval(v.ruleparamtbname)
#
#            ruleparamlist = session.query(model).filter(model.Id == int(v.ruleparamid)).all()
#
#            #删除工位数据
#
#            session.delete(v.analysisarea)
#
#            #删除关联的规则数据
#
#            for param in ruleparamlist:
#
#                session.delete(param)
#
#
#            #删除工位与规则的关联关系
#
#            session.delete(v)
#
#    return 1,'ok'
#
#
#def AddWorkpos_db(session,newworkpos):
#    session.add(newworkpos)
#
#
#
#def UpdateRuleparam_db(session,tbname,ruleparamid,data_dict):
#    model = eval(tbname)
#    session.query(model).filter(model.Id== int(ruleparamid)).update(data_dict)
#
#
#
#
#
#
#def UpdateArea_Rule_db(session,ruleparamid,ruletypeid,data_dict):
#    d=session.query(alys_ruletype).filter(and_(alys_ruletype.ruleparamid== int(ruleparamid),alys_ruletype.ruletypeid==int(ruletypeid)) )
#    d.update(data_dict)
#
#
#
#
#def AddRuleparam_db(session,newruleparam):
#    session.add(newruleparam)
#
#
#
#
#def AddArea_Rule_db(session,newArea_Rule):
#
#    session.add(newArea_Rule)
#
#
#
##endregion
#
##region  video source
#
#def Getvideoinfo_db(session,sqlwhere=''):
#    if sqlwhere=='':
#        result = session.query(videoSource).all()
#    else:
#        result = session.query(videoSource).filter(text(sqlwhere)).all()
#    return result
#
#
#def select_VideoInfoByPage(session,PageIndex,PageSize=10,sqlwhere=''):
#    '''
#       对非常规行为进行分页查询
#       :param PageIndex: 页索引值
#       :param PageSize: 每页显示数量
#       :param sqlwhere:筛选条件
#       :return:返回分页数据集和总的记录数
#    '''
#    if sqlwhere != '':
#        total= session.query(videoSource).order_by(videoSource.id).filter(text(sqlwhere)).count()
#        data= session.query(videoSource).order_by(videoSource.id).filter(text(sqlwhere)).limit(PageSize).offset(PageIndex).all()
#    else:
#        total = session.query(videoSource).order_by(videoSource.id).count()
#        data = session.query(videoSource).order_by(videoSource.id).limit(PageSize).offset(PageIndex).all()
#    return (total,data),1,'ok'
#
#
#def Addvideo_db(session,video):
#    session.add(video)
#
#
#def Updatevideo_db(session,videoid,update_data):
#    d=session.query(videoSource).filter(videoSource.id == videoid)
#    d.update(update_data)
#
#
#def Delvideo_db(session,videoid):
#    curvideos= session.query(videoSource).filter(videoSource.id == videoid).all()
#    session.delete(curvideos[0])
#
#
##endregion
#
##region Alarm
#def select_AlarmByPage(session,PageIndex,PageSize=10,sqlwhere=''):
#    '''
#       对视频源进行分页查询
#       :param PageIndex: 页索引值
#       :param PageSize: 每页显示数量
#       :param sqlwhere:筛选条件
#       :return:返回分页数据集和总的记录数
#    '''
#    if sqlwhere != '':
#        total=session.query(alarm,alys_ruletype,analysisarea,videoSource).join(alys_ruletype,and_(alarm.ruletypeid==alys_ruletype.ruletypeid,alarm.ruleparamid==alys_ruletype.ruleparamid) ).join(analysisarea,alys_ruletype.analysisareaid==analysisarea.id).join(videoSource,analysisarea.videoid==videoSource.id).filter(text(sqlwhere)).count()
#        d= session.query(alarm,alys_ruletype,analysisarea,videoSource).join(alys_ruletype,and_(alarm.ruletypeid==alys_ruletype.ruletypeid,alarm.ruleparamid==alys_ruletype.ruleparamid) ).join(analysisarea,alys_ruletype.analysisareaid==analysisarea.id).join(videoSource,analysisarea.videoid==videoSource.id).filter(text(sqlwhere)).order_by(desc(alarm.alerttime)).limit(PageSize).offset(PageIndex)
#        data=d.all()
#    else:
#        total = session.query(alarm, alys_ruletype, analysisarea, videoSource).join(alys_ruletype, and_(alarm.ruletypeid == alys_ruletype.ruletypeid, alarm.ruleparamid == alys_ruletype.ruleparamid)).join(analysisarea, alys_ruletype.analysisareaid == analysisarea.id).join(videoSource,analysisarea.videoid == videoSource.id).count()
#
#        data =  session.query(alarm, alys_ruletype, analysisarea, videoSource).join(alys_ruletype, and_(alarm.ruletypeid == alys_ruletype.ruletypeid, alarm.ruleparamid == alys_ruletype.ruleparamid)).join(analysisarea, alys_ruletype.analysisareaid == analysisarea.id).join(videoSource,analysisarea.videoid == videoSource.id).order_by(desc(alarm.alerttime)).limit(PageSize).offset(PageIndex).all()
#
#    return (total,data)
#
#
#
#def select_Alarm2(session,sqlwhere=''):
#    '''
#       更详细的报警信息
#       :param sqlwhere:筛选条件
#       :return:总集合
#    '''
#    if sqlwhere != '':
#        result=session.query(alarm,alys_ruletype,analysisarea,videoSource).join(alys_ruletype,and_(alarm.ruletypeid==alys_ruletype.ruletypeid,alarm.ruleparamid==alys_ruletype.ruleparamid) ).join(analysisarea,alys_ruletype.analysisareaid==analysisarea.id).join(videoSource,analysisarea.videoid==videoSource.id).filter(text(sqlwhere)).all()
#    else:
#        result = session.query(alarm, alys_ruletype, analysisarea, videoSource).join(alys_ruletype, and_(alarm.ruletypeid == alys_ruletype.ruletypeid, alarm.ruleparamid == alys_ruletype.ruleparamid)).join(analysisarea, alys_ruletype.analysisareaid == analysisarea.id).join(videoSource,analysisarea.videoid == videoSource.id).all()
#
#    return result
#
#
#
#def select_Alarm(session,sqlwhere=''):
#    if sqlwhere=='':
#        result = session.query(alarm).all()
#    else:
#        result = session.query(alarm).filter(text(sqlwhere)).all()
#    return result
#
#
##endregion
#
##region sysparam
#
#def select_sysparam_db(session,sqlwhere=''):
#    if sqlwhere == '':
#        result = session.query(param).all()
#    else:
#        result = session.query(param).filter(text(sqlwhere)).all()
#    return result
#
#def select_sysparamtype_db(session,sqlwhere=''):
#    if sqlwhere == '':
#        result = session.query(paramtype).all()
#    else:
#        result = session.query(paramtype).filter(text(sqlwhere)).all()
#    return result
#
#
#def update_sysparam_db(session,id,data_dict):
#    session.query(param).filter(param.id == int(id)).update(data_dict)
#
##endregion
#
##region timeplan
#
#def SelectTimePlan_db(session,sqlwhere):
#    if sqlwhere == '':
#        result = session.query(timeplan).order_by(timeplan.starttime).all()
#    else:
#        d=session.query(timeplan).filter(text(sqlwhere)).order_by(timeplan.starttime)
#
#        result = d.all()
#    return result
#
#def GetPlanTemplate_db(session,sqlwhere=''):
#    sql='select  * from tbl_template  ORDER BY name '
#    result=session.execute(sql).fetchall()
#    return result
#
#
#
#def Addtimeplan_db(session,plan):
#    session.add(plan)
#
#def Update_timeplan_db(session,planid,update_data):
#    d=session.query(timeplan).filter(timeplan.id == planid)
#    d.update(update_data)
#
#
#def Del_timeplan_db(session,templateid):
#    curplans= session.query(timeplan).filter(timeplan.templateid == templateid).all()
#    for v in curplans:
#        session.delete(v)
#        # session.delete(v.template)
#
#    # curtpls=session.query(timetemplate).filter(timetemplate.id==templateid).all()
#    # for v in curtpls:
#    #     session.delete(v)


#endregion













