import urllib.request
import xml.etree.ElementTree as ET

url = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey=tKz%2FiLxyD78ft6XbyWnmfh6IyIFaWnxkJhXFfI6FG%2FdrkA41IfPwKJ2LSGp9yHh6bKX0%2F5YeNJWnt1tPUmIXBg%3D%3D&arsId=02218"

data = urllib.request.urlopen(url).read()


file_name = "bussopt.xml"
f_ = open(file_name, "wb")  # 다른 사람들의 예제처럼 "w"만 해서 했더니 에러가 발생
f_.write(data)
f_.close()

doc=ET.parse(file_name)
root=doc.getroot()

for a in root.iter("itemList"):
    adirection = a.findtext("adirection")
    arrmsg1 = a.findtext("arrmsg1")
    arrmsg2 = a.findtext("arrmsg2")

    nxtStn  = a.findtext("nxtStn")
    sectNm  = a.findtext("sectNm")
    stNm  = a.findtext("stNm")
    gpsX = a.findtext("gpsX")
    gpsY = a.findtext("gpsY")

    print("방향:"+adirection)
    print("도착예정: "+arrmsg1)
    print("다음 도착예정: "+arrmsg2)

    print("다음정류장:"+nxtStn)
    print("구간:"+sectNm)
    print("검색한 근처 정류장:"+stNm)
    print(gpsX)
    print(gpsY)
    print("--------------------")


