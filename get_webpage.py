import requests 
from enuminfo import flowto

class  requestHelper(object):
    def __init__(self,date,citycode,flowto):
        self.date=date
        self.citycode=citycode
        self.flowto=flowto

    def get_cookie(self):
        cookie_dict={}
        cookie_dict["access-control-allow-headers"]=r"Origin; No-Cache; X-Requested-With; If-Modified-Since; Pragma; Last-Modified; Cache-Control; Expires; Content-Type; Content-Language; Cache-Control; X-E4M-With"
        cookie_dict["access-control-allow-origin"]=r"*"
        cookie_dict["cache-control"]=r"max-age=86400"
        cookie_dict["content-encoding"]=r"gzip"
        cookie_dict["content-type"]=r"application/x-javascript"
        cookie_dict["date"]=r"Sun, 30 Dec 2018 15:10:31 GMT"
        cookie_dict["etag"]=r"W/'5c27cb18-17c'"
        cookie_dict["expires"]=r"Mon, 31 Dec 2018 15:10:30 GMT"
        cookie_dict["last-modified"]=r"Sat, 29 Dec 2018 19:29:28 GMT"
        cookie_dict["server"]=r"NWSs"
        cookie_dict["status"]="200"
        cookie_dict["x-cache-lookup"]=r"Hit From Upstream"
        cookie_dict["x-nws-log-uuid"]=r"32bb93ca-0ff0-440c-b2b7-9c2b431ca246"
        return cookie_dict

    def getUrl(self):
        if self.flowto==flowto.flowout:
            url=r"https://lbs.gtimg.com/maplbs/qianxi/%s/%s16.js?callback=JSONP_LOADER&_=1546936585552"%(self.date,self.citycode)
        else:
            url=r"https://lbs.gtimg.com/maplbs/qianxi/%s/%s06.js?callback=JSONP_LOADER&_=1546936585552"%(self.date,self.citycode)
        print(url)
        return url

    def get_rawdata(self):
        url=self.getUrl()
        cookie=self.get_cookie()
        return requests.get(url,cookies=cookie)
