from urllib import parse
import urllib.request
import xml.etree.ElementTree as etree

from tkinter import *
from tkinter import font
from tkinter import ttk


global encoding
key=None

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
}

#encoding = parse.quote(Line_four["정왕"])

def Init_Top_Text(): #메인 텍스트
    temp_font = font.Font(window, size=20, weight="bold", family="Consolas")
    MainText = Label(window,font=temp_font,text="[4호선 지하철 검색APP]")
    MainText.pack()
    MainText.place(x=350,y=20)

def InitSearch_Island_Platform():#지하철 상하행 알려주는 옵션
    global SearchListBox
    Search_Scrollbar=Scrollbar(window)
    Search_Scrollbar.pack()
    Search_Scrollbar.place(x=360,y=100)

    temp_font = font.Font(window, size=13, weight="bold", family="Consolas")
    SearchListBox = Listbox(window, font=temp_font, activestyle="none", width=10, height=1, borderwidth=10,relief="ridge", yscrollcommand=Search_Scrollbar.set)

    SearchListBox.insert(1, "상행")
    SearchListBox.insert(2, "하행")
    SearchListBox.insert(3, "상하행")
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
    global  encoding,ok_butten_ck,sbway_name_search,print_sbway_list_box,SearchListBox
    ok_butten_ck=True
    sbway_name = str(sbway_name_search.get())
    if (ok_butten_ck):
        encoding = parse.quote(Line_four[sbway_name])
        ok_butten_ck = False

    print_sbway_list_box.configure(state='normal')
    print_sbway_list_box.delete(0,END)
    Print_Sbway_List_Box()
    # iSearchIndex = SearchListBox.curselection()[3]
    # if iSearchIndex == 1:
    #     abc()
    #     pass
    # elif iSearchIndex == 2:
    #     pass
    # elif iSearchIndex == 3:
    #     pass
    #print_sbway_list_box.configure(state='disabled')


def Print_Sbway_List_Box(): #지하철 정보
    global root,window,root,sbway_name,encoding
    # 서울공공데이터사용
    key = "616d6b51456a6b7939324b4f626948"
    url = "http://swopenapi.seoul.go.kr/api/subway/sample/xml/realtimeStationArrival/1/5/" + encoding

    data = urllib.request.urlopen(url).read()

    filename = "sample1.xml"
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
        print_sbway_list_box.insert(0, "내리실 문: " + present_door)
        print_sbway_list_box.insert(0, "지하철 위치: " + current_position)
        print_sbway_list_box.insert(0, "몇전역: "+arvlMsg)
        print_sbway_list_box.insert(0, "방향: " + begine_end_sbway)
        print_sbway_list_box.insert(0, division)

def abc():
    for a in root.findall("row"):
        begine_end_sbway = a.findtext("trainLineNm")
        arvlMsg = a.findtext("arvlMsg2")
        current_position = a.findtext("arvlMsg3")
        present_door =a.findtext("subwayHeading")
        division ="-------------------"
        print_sbway_list_box.insert(0, "내리실 문: " + present_door)
        print_sbway_list_box.insert(0, "지하철 위치: " + current_position)
        print_sbway_list_box.insert(0, "몇전역: "+arvlMsg)
        print_sbway_list_box.insert(0, "방향: " + begine_end_sbway)
        print_sbway_list_box.insert(0, division)

def Init_Print_Sbway_List_Box(): #GUI
    global print_sbway_list_box
    temp_font = font.Font(window, size=15, weight="bold", family="Consolas")
    print_sbway_scrollbar = Scrollbar(window)
    print_sbway_scrollbar.pack(side="right", fill="y")
    # print_sbway_scrollbar.place(x=420, y=150)

    print_sbway_list_box = Listbox(window, font=temp_font, width=34, height=25,
                                   yscrollcommand=print_sbway_scrollbar.set)
    print_sbway_list_box.pack()
    print_sbway_list_box.place(x=40, y=150)
    print_sbway_scrollbar.config(command=print_sbway_list_box.yview)

def Map():#지도 구성
    import folium
    #정왕역
    위도 = 37.351770
    경도 = 126.7418618
    map = folium.Map(location=[위도, 경도],
                     tiles="OpenStreetMap",
                     zoom_start=30)

    folium.Marker( #마커 크롤링 해서 딕셔너리 넣던지 다 저장해서 출력해야함.
        location=[위도,경도],
        popup="Marker Here",
        icon=folium.Icon(icon='green')
    ).add_to(map)
    map.save('map.html')

def Map_event(): #지도 저장
    import webbrowser
    url = 'map.html'
    webbrowser.open(url)


def Map_Butten(): #지도열기
    mapbutten=Button(window,text="지도열기",command=Map_event)
    mapbutten.pack()
    pass


Init_Top_Text() #메인 텍스트
InitSearch_Island_Platform() #지하철 상하행 알려주는 옵션
Init_Input_Label() #지하철 검색창
Init_Search_Button() #지하철 검색 버튼
Init_Print_Sbway_List_Box()#지하철 정보 GUI

Map()
Map_Butten()

window.mainloop()
