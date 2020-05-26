from urllib import parse
import urllib.request
import xml.etree.ElementTree as etree
from tkinter import *
from tkinter import font

# parse.quote('정왕') 예시
def encoding_line():
    global encoding
    Line_four = {  # 역 명 딕셔너리
        'NULL':None
        ,'오이도': '오이도'
        , '정왕': '정왕'
        , '신길온천': '신길온천'
        , '안산': '안산'
        , '초지': '초지'
        , '고잔': '고잔'
        , '중앙': '중앙'
        , '한대앞': '한대앞'
        , '상록수': '상록수'
        , '반월': '반월'
        , '대야미': '대야미'
        , '수리산': '수리산'
        , '산본': '산본'
        , '금정': '금정'
        , '범계': '범계'
        , '평촌': '평촌'
        , '인덕원': '인덕원'
        , '정부과청청사': '정부과천청사'
        , '과천': '과천'
        , '대공원': '대공원'
        , '경마공원': '경마공원'
        , '선바위': '선바위'
        , '남태령': '남태령'
        , '사당': '사당'
        , '총신대입구': '총신대입구'
        , '동작': '동작'
        , '이촌': '이촌'
        , '신용산': '신용산'
        , '삼각지': '삼각지'
        , '숙대입구': '숙대입구'
        , '서울역': '서울역'
        , '회연': '회연'
        , '명동': '명동'
        , '충무로': '충무로'
        , '동대문역사문화공원': '동대문역사문화공원'
        , '동대문': '동대문'
        , '혜화': '혜화'
        , '한성대입구': '한성대입구'
        , '성신여대입구': '성신여대입구'
        , '길음': '길음'
        , '미아사거리': '미아사거리'
        , '미아': '미아'
        , '수유': '수유'
        , '쌍문': '쌍문'
        , '창동': '창동'
        , '노원': '노원'
        , '상계': '상계'
        , '당고개': '당고개'
    }
    encoding = parse.quote(Line_four['정왕'])


def main():
    global encoding,sbway_name_search,sbway_name_search2
    # GUI
    window = Tk()
    window.geometry("400x600+750+200")  # GUI 크기

    sbway_name_search = Entry(window)
    sbway_name_search.pack()
    sbway_name_search2 = Entry(window)
    sbway_name_search2.pack()
    ok_butten = Button(window, text='확인',command=Sbway_Name_Search)
    ok_butten.pack()


    # 서울공공데이터사용
    key = '616d6b51456a6b7939324b4f626948'
    url = "http://swopenapi.seoul.go.kr/api/subway/sample/xml/realtimeStationArrival/1/5/" + encoding

    data = urllib.request.urlopen(url).read()

    filename = "sample1.xml"
    f = open(filename, "wb")  # 다른 사람들의 예제처럼 "w"만 해서 했더니 에러가 발생
    f.write(data)
    f.close()

    # 파싱하기
    tree = etree.parse(filename)
    root = tree.getroot()

    for a in root.findall('row'):
        begine_end_sbway = Label(window, text=a.findtext('trainLineNm'))
        begine_end_sbway.pack()
        arvlMsg = Label(window, text=a.findtext('arvlMsg2'))
        arvlMsg.pack()
        current_position = Label(window, text=a.findtext('arvlMsg3'))
        current_position.pack()
        present_door = Label(window, text=a.findtext('subwayHeading'))
        present_door.pack()

    window.mainloop()

def Sbway_Name_Search():
    global sbway_name_search, sbway_name_search2,encoding

    sbway_name =str(sbway_name_search.get())
    sbway_name_search2.insert(0, str(sbway_name))
    pass




if __name__ == "__main__":
    encoding_line()
    Sbway_Name_Search
    main()
