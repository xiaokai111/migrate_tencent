from get_webpage import requestHelper
import re,json

class parseHelper(object):
    def __init__(self,rqt):
        self.requesthelper=rqt
    def cleandata(self):
        raw_data=self.requesthelper.get_rawdata()
        print(raw_data.text)
        m=re.match(r'.*\(\[(.*)\,\]\)$',raw_data.text)
        jsonstr=m.group(1)
        jsonstr='[%s]'%jsonstr
        data_dict=json.loads(jsonstr)
        return data_dict

