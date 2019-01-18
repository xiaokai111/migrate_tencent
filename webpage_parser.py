from get_webpage import requestHelper
import re,json,os
class parseHelper(object):
    def __init__(self,rqt):
        self.requesthelper=rqt
    def cleandata(self):
        raw_data=self.requesthelper.get_rawdata()
        try:
            if raw_data.status_code!=200:
                raise Exception('status_code:%d'%raw_data.status_code)
        except Exception as e:
            print(e.args)
            os._exit(0)
        m=re.match(r'.*\(\[(.*)\,\]\)$',raw_data.text)
        jsonstr=m.group(1)
        jsonstr='[%s]'%jsonstr
        data_dict=json.loads(jsonstr)
        return data_dict

