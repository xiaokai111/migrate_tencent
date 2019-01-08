# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

def GetPathDB_sqlite():
    data_path = r'sqlite:///' + basedir
    data_path = GetParentPath(data_path, 2) + r'/data.hsdb'
    print(data_path)
    return data_path


def GetPathDB_Mysql():
    #本机
    data_path = 'mysql+pymysql://username:password@127.0.0.1:port/dbname?charset=utf8'
    return data_path

