# Create your models here.
from sqlalchemy import Column, String, create_engine,Integer,DateTime,NUMERIC,ForeignKey,Boolean,Numeric,PrimaryKeyConstraint,UniqueConstraint,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm  import  relationship,backref,validates
Base = declarative_base()

class region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer,nullable=False)
    description = Column(String)
    code = Column(String(32))
    name=Column(String)
    sequence=Column(Integer)
    level=Column(Integer)
    initial=Column(CHAR)
    acronym=Column(String)
    pinyin=Column(String)
    is_enabled=Column(Integer)
    create_date=Column(DateTime)
    create_user=Column(String)
    update_user=Column(String)
    update_date=Column(DateTime)
    # alys_ruletype = relationship("alys_ruletype")
    # rules = relationship("alys_ruletype", backref="tbl_analysisarea")

class result(Base):
    __tablename__ = 'result'
    __table_args__ = (
        PrimaryKeyConstraint('date', 'dep_citycode','des_citycode'),
    )
    ALLOWED_APP_ESSAY_STATES = ["selected", "not_selected", "pending"]
    date = Column(String)
    dep_citycode=Column(Integer)
    departure=Column(String)
    des_citycode=Column(Integer)
    destination=Column(String)
    total=Column(Integer)
    heatvalue=Column(NUMERIC)
    bus_persontime=Column(Integer)
    bus_proportion=Column(NUMERIC)
    train_persontime=Column(Integer)
    train_proportion=Column(NUMERIC)
    airplane_persontime=Column(Integer)
    airplane_proportion=Column(NUMERIC)
class result_inflow(Base):
    __tablename__ = 'result_inflow'
    __table_args__ = (
        PrimaryKeyConstraint('date', 'dep_citycode','des_citycode'),
    )
    ALLOWED_APP_ESSAY_STATES = ["selected", "not_selected", "pending"]
    date = Column(String)
    dep_citycode=Column(Integer)
    departure=Column(String)
    des_citycode=Column(Integer)
    destination=Column(String)
    total=Column(Integer)
    heatvalue=Column(NUMERIC)
    bus_persontime=Column(Integer)
    bus_proportion=Column(NUMERIC)
    train_persontime=Column(Integer)
    train_proportion=Column(NUMERIC)
    airplane_persontime=Column(Integer)
    airplane_proportion=Column(NUMERIC)

class result_flowout(Base):
    __tablename__ = 'result_flowout'
    __table_args__ = (
        PrimaryKeyConstraint('date', 'dep_citycode','des_citycode'),
    )
    ALLOWED_APP_ESSAY_STATES = ["selected", "not_selected", "pending"]
    date = Column(String)
    dep_citycode=Column(Integer)
    departure=Column(String)
    des_citycode=Column(Integer)
    destination=Column(String)
    total=Column(Integer)
    heatvalue=Column(NUMERIC)
    bus_persontime=Column(Integer)
    bus_proportion=Column(NUMERIC)
    train_persontime=Column(Integer)
    train_proportion=Column(NUMERIC)
    airplane_persontime=Column(Integer)
    airplane_proportion=Column(NUMERIC)
