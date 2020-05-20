
import urllib.request
import xml.etree.ElementTree as etree

def main():

    #서울공공데이터사용
    Jeongwang = '%EC%A0%95%EC%99%95'
    key = '616d6b51456a6b7939324b4f626948'
    url = "http://swopenapi.seoul.go.kr/api/subway/sample/xml/realtimeStationArrival/1/5/"+Jeongwang

    data = urllib.request.urlopen(url).read()

    filename = "sample1.xml"
    f = open(filename, "wb") #다른 사람들의 예제처럼 "w"만 해서 했더니 에러가 발생
    f.write(data)
    f.close()

    #파싱하기
    tree = etree.parse(filename)
    root = tree.getroot()

    for a in root.findall('row'):
        print(a.findtext('trainLineNm'))
        print(a.findtext('arvlMsg2'))
        print(a.findtext('arvlMsg3'))
        print(a.findtext('subwayHeading'))
        print('----------------------')


if __name__ == "__main__":
    main()