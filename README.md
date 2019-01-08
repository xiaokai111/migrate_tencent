# migrate_tencent
爬取腾讯迁徙的人流数据

#安装python库
‘’‘
pip install -r requirements.txt
’‘’

#配置数据库
+将DBconfig.bak.py更名为DBconfig.py （因GetPathDB_Mysql为个人的配置含有私密数据所有没有上传）
+打开更名后的文件DBconfig.py，将GetPathDB_Mysql函数里面的username替换成你的mysql的用户名，password替换成你的mysql的密码，127.0.0.1为你的mysql的IP地址，
 port为你的mysql端口号，一般为3306，dbname为你的数据库名字
 
#运行
'''
python run.py -s 20180101  -e 20180201 -n 武汉
'''

