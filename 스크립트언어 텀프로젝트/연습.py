from urllib import parse
import urllib.request
import xml.etree.ElementTree as etree

from tkinter import *
from tkinter import font
from tkinter import ttk


global coding,busnumber
key = "616d6b51456a6b7939324b4f626948"
ok_butten_ck=False

window = Tk()
window.geometry("1000x800")  # GUI 크기
window.title("4호선 지하철 검색")


Line_four = {  # 역 명 딕셔너리
        "NULL":" "
        ,"오이도": "오이도"
        , "정왕": "정왕"
        , "신길온천": "신길온천"
        , "안산": "안산"
        , "초지": "초지"
        , "고잔": "고잔"
        , "중앙": "중앙"
        , "한대앞": "한대앞"
        , "상록수": "상록수"
        , "반월": "반월"
        , "대야미": "대야미"
        , "수리산": "수리산"
        , "산본": "산본"
        , "금정": "금정"
        , "범계": "범계"
        , "평촌": "평촌"
        , "인덕원": "인덕원"
        , "정부과청청사": "정부과천청사"
        , "과천": "과천"
        , "대공원": "대공원"
        , "경마공원": "경마공원"
        , "선바위": "선바위"
        , "남태령": "남태령"
        , "사당": "사당"
        , "총신대입구": "총신대입구"
        , "동작": "동작"
        , "이촌": "이촌"
        , "신용산": "신용산"
        , "삼각지": "삼각지"
        , "숙대입구": "숙대입구"
        , "서울" : "서울"
        , "서울역": "서울"
        , "회연": "회연"
        , "명동": "명동"
        , "충무로": "충무로"
        , "동대문역사문화공원": "동대문역사문화공원"
        , "동대문": "동대문"
        , "혜화": "혜화"
        , "한성대입구": "한성대입구"
        , "성신여대입구": "성신여대입구"
        , "길음": "길음"
        , "미아사거리": "미아사거리"
        , "미아": "미아"
        , "수유": "수유"
        , "쌍문": "쌍문"
        , "창동": "창동"
        , "노원": "노원"
        , "상계": "상계"
        , "당고개": "당고개"
        , "평택":"평택"
}


number = {  # 역 명 딕셔너리
        "NULL":" "
        , "수리산": "1763"
        , "산본": "1751"
        , "금정": "1458"
        , "범계": "1457"
        , "인덕원": "1455"
        , "정부과청청사": "1454"
        , "과천": "1453"
        , "선바위": "1450"
        , "남태령": "0434"
        , "사당": "0433"
        , "총신대입구": "0432"
        , "동작": "0431"
        , "이촌": "0430"
        , "신용산": "0429"
        , "삼각지": "0428"
        , "숙대입구": "0427"
        , "서울" : "0426"
        , "서울역": "0426"
        , "회연": "0425"
        , "명동": "0424"
        , "충무로": "0423"
        , "동대문역사문화공원": "0422"
        , "동대문": "421"
        , "혜화": "0420"
        , "한성대입구": "0419"
        , "성신여대입구": "0418"
        , "길음": "0417"
        , "미아사거리": "0416"
        , "미아": "0415"
        , "수유": "0414"
        , "쌍문": "0413"
        , "창동": "0412"
        , "노원": "0411"
        , "상계": "0410"
        , "당고개": "0409"
}


def Init_Top_Text(): #메인 텍스트
    temp_font = font.Font(window, size=20, weight="bold", family="Consolas")
    MainText = Label(window,font=temp_font,text="[대중교통 정보 서비스]")
    MainText.pack()
    MainText.place(x=350,y=20)

def InitSearch_Island_Platform():#지하철 상하행 알려주는 옵션
    global SearchListBox
    Search_Scrollbar=Scrollbar(window)
    Search_Scrollbar.pack()
    Search_Scrollbar.place(x=360,y=100)

    temp_font = font.Font(window, size=13, weight="bold", family="Consolas")
    SearchListBox = Listbox(window, font=temp_font, activestyle="none", width=10, height=1, borderwidth=10,relief="ridge", yscrollcommand=Search_Scrollbar.set)

    SearchListBox.insert(1, "지하철")
    SearchListBox.insert(2, "버스")
    SearchListBox.pack()
    SearchListBox.place(x=250, y=100)
    Search_Scrollbar.config(command=SearchListBox.yview)
    pass

def Init_Input_Label(): #지하철역 검색창
    global sbway_name_search
    sbway_name_search_font = font.Font(window,size=13,weight="bold",family="Consolas")
    sbway_name_search = Entry(window,font=sbway_name_search_font,width=20,borderwidth=10,state="normal")
    sbway_name_search.pack()
    sbway_name_search.place(x=40,y=100)


def Init_Search_Button(): #지하철역 검색 확인버튼
    global ok_butten_ck
    ok_butten = Button(window, text="검색",command=SearchButtonAction)
    ok_butten.pack()
    ok_butten.place(x=380, y=110)
    ok_butten.configure(font='helvetiac 15')



def SearchButtonAction(): #지하철 검색액션
    global  coding,ok_butten_ck,sbway_name_search,print_list_box,SearchListBox
    ok_butten_ck=True
    iSearchIndex = SearchListBox.curselection()

    if (len(iSearchIndex)) == 0:
        isearchindex1()
        print(len(iSearchIndex))

    elif (len(iSearchIndex)) == 1:
        isearchindex2()
        print(len(iSearchIndex))



    print_list_box.configure(state='normal')

def isearchindex1():
    global coding,ok_butten_ck,sbway_name_search,print_list_box,busnumber
    sbway_name = str(sbway_name_search.get())
    if (ok_butten_ck):
        coding = parse.quote(Line_four[sbway_name])
        ok_butten_ck = False

    print_list_box.configure(state='normal')
    print_list_box.delete(0, END)
    Print_Sbway_List_Box()
    maps(sbway_name)

def isearchindex2():
    global busnumber, ok_butten_ck, sbway_name_search, print_list_box,coding,GPS
    sbway_name = str(sbway_name_search.get())
    if (ok_butten_ck):
        coding = parse.quote(Line_four[sbway_name])
        ok_butten_ck = False

    print_list_box.configure(state='normal')
    print_list_box.delete(0, END)
    Print_Bus_List_Box()
    maps(sbway_name)



def Print_Sbway_List_Box(): #지하철 정보
    global root,window,root,sbway_name,coding
    # 서울공공데이터사용

    url = "http://swopenapi.seoul.go.kr/api/subway/sample/xml/realtimeStationArrival/1/5/" + coding

    data = urllib.request.urlopen(url).read()

    filename = "sbway.xml"
    f = open(filename, "wb")  # 다른 사람들의 예제처럼 "w"만 해서 했더니 에러가 발생
    f.write(data)
    f.close()

    # 파싱하기
    tree = etree.parse(filename)
    root = tree.getroot()
    for a in root.findall("row"):
        begine_end_sbway = a.findtext("trainLineNm")
        arvlMsg = a.findtext("arvlMsg2")
        current_position = a.findtext("arvlMsg3")
        present_door =a.findtext("subwayHeading")
        division ="-------------------"
        print_list_box.insert(0, "내리실 문: " + present_door)
        print_list_box.insert(0, "지하철 위치: " + current_position)
        print_list_box.insert(0, "몇전역: " + arvlMsg)
        print_list_box.insert(0, "방향: " + begine_end_sbway)
        print_list_box.insert(0, division)


def Print_Bus_List_Box(): #버스 정보
    global busnumber,coding
    import urllib.request
    import xml.etree.ElementTree as ET

    url = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByName?serviceKey=tKz%2FiLxyD78ft6XbyWnmfh6IyIFaWnxkJhXFfI6FG%2FdrkA41IfPwKJ2LSGp9yHh6bKX0%2F5YeNJWnt1tPUmIXBg%3D%3D&stSrch=" + coding
    data = urllib.request.urlopen(url).read()

    file_name = "bus.xml"
    f_ = open(file_name, "wb")  # 다른 사람들의 예제처럼 "w"만 해서 했더니 에러가 발생
    f_.write(data)
    f_.close()

    doc = ET.parse(file_name)
    root = doc.getroot()
    for a in root.iter("itemList"):
        arsId = a.findtext("arsId")
        print(arsId)
        Bus_Stop(arsId)



def Bus_Stop(arsId):
    global BusGpsX,BusGpsY
    import urllib.request
    import xml.etree.ElementTree as ET

    url = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey=tKz%2FiLxyD78ft6XbyWnmfh6IyIFaWnxkJhXFfI6FG%2FdrkA41IfPwKJ2LSGp9yHh6bKX0%2F5YeNJWnt1tPUmIXBg%3D%3D&arsId="+arsId

    data = urllib.request.urlopen(url).read()

    file_name = "bussopt.xml"
    f_ = open(file_name, "wb")  # 다른 사람들의 예제처럼 "w"만 해서 했더니 에러가 발생
    f_.write(data)
    f_.close()

    doc = ET.parse(file_name)
    root = doc.getroot()

    for a in root.iter("itemList"):
        adirection = a.findtext("adirection")
        arrmsg1 = a.findtext("arrmsg1")
        arrmsg2 = a.findtext("arrmsg2")
        nxtStn = a.findtext("nxtStn")
        sectNm = a.findtext("sectNm")
        stNm = a.findtext("stNm")
        BusGpsX = a.findtext("gpsX")
        BusGpsY = a.findtext("gpsY")
        division ="-------------------"
        print_list_box.insert(0, "구간:" + sectNm)
        print_list_box.insert(0,"방향:"+adirection)
        print_list_box.insert(0,"다음정류장:"+nxtStn)
        print_list_box.insert(0, "다음 도착예정: " + arrmsg2)
        print_list_box.insert(0, "도착예정: " + arrmsg1)
        print_list_box.insert(0,"검색한 근처 정류장:"+stNm)
        print_list_box.insert(0,division)


def Init_Print_Sbway_List_Box(): #GUI
    global print_list_box
    temp_font = font.Font(window, size=15, weight="bold", family="Consolas")
    print_sbway_scrollbar = Scrollbar(window)
    print_sbway_scrollbar.pack(side="right", fill="y")
    # print_sbway_scrollbar.place(x=420, y=150)

    print_list_box = Listbox(window, font=temp_font, width=34, height=25,
                             yscrollcommand=print_sbway_scrollbar.set)
    print_list_box.pack()
    print_list_box.place(x=40, y=150)
    print_sbway_scrollbar.config(command=print_list_box.yview)

def Map(sbway_name):#지도 구성
    import folium
    #정왕역
    map = folium.Map(location=[float(SbwayGpsX), float(SbwayGpsY)],
                     tiles="OpenStreetMap",
                     zoom_start=30)

    folium.Marker(
        location=[float(SbwayGpsX),float(SbwayGpsY)],
        popup=sbway_name+"역",
        icon=folium.Icon(icon='green')
    ).add_to(map)

def Map_event(): #지도 저장
    import webbrowser
    url = 'map.html'
    webbrowser.open(url)


def Map_Butten(): #지도열기
    mapbutten=Button(window,text="지도열기",command=Map_event)
    mapbutten.pack()
    pass

def maps(sbway_name):
    global SbwayGpsX,SbwayGpsY,line,GPS
    import csv
    f = open('4호선 지하철 역 위치정보.csv', 'rt', encoding='UTF8')
    rdr = csv.reader(f)
    for line in rdr:
        if (line[0] == sbway_name):
                SbwayGpsX=line[1]
                SbwayGpsY=line[2]
    f.close()
    Map(sbway_name)

def Gmail(): #Gmail 보내기 GUI

    Lable_login = Label(window, text="Gmail 로그인",font='helvetica 16 italic',width=15, borderwidth=5,relief="ridge")
    Lable_login.pack()
    Lable_login.place(x=650, y=450)

    Lable_id = Label(window, text="ID:")
    Lable_id.pack()
    Lable_id.place(x=625, y=505)

    Lable_pw = Label(window, text="PW:")
    Lable_pw.pack()
    Lable_pw.place(x=625, y=555)

    #id
    temp_font = font.Font(window, size=13,family="Consolas")
    Entry_id = Entry(window, font=temp_font, width=20, borderwidth=3,relief="solid")
    Entry_id.pack()
    Entry_id.place(x=650, y=500)

    #pw
    temp_font = font.Font(window, size=13, family="Consolas")
    Entry_pw = Entry(window, font=temp_font, width=20, borderwidth=3,relief="solid")
    Entry_pw.pack()
    Entry_pw.place(x=650, y=550)


    pass





Init_Top_Text() #메인 텍스트
InitSearch_Island_Platform() #지하철 상하행 알려주는 옵션
Init_Input_Label() #지하철 검색창
Init_Search_Button() #지하철 검색 버튼
Init_Print_Sbway_List_Box()#지하철 정보 GUI
Map_Butten()
Gmail()
window.mainloop()
