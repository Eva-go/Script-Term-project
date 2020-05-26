from urllib import parse
import urllib.request
import xml.etree.ElementTree as etree

from tkinter import *
from tkinter import font
import tkinter.messagebox

# parse.quote("정왕") 예시
global encoding
key=None
Line_four = {  # 역 명 딕셔너리
        "NULL":None
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
        , "서울":"서울역"
        , "서울역": "서울역"
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
encoding = parse.quote(Line_four["정왕"])

def API():
    global window,root
    import http.client
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



def Init_Top_Text(): #메인 텍스트
    temp_font = font.Font(window, size=20, weight="bold", family="Consolas")
    MainText = Label(window,font=temp_font,text="[4호선 지하철 검색APP]")
    MainText.pack()
    MainText.place(x=20)


def Init_Input_Label(): #지하철역 검색
    global sbway_name_search
    sbway_name_search_font=font.Font(window,size=15,weight="bold",family="Consolas")
    sbway_name_search = Entry(window,font=sbway_name_search_font,width=26,borderwidth=12,state="normal")
    sbway_name_search.pack()

def Init_Search_Button(): #지하철역 검색 확인버튼
    ok_butten = Button(window, text="검색", command=Sbway_Name_Search)
    ok_butten.pack()

def InitSearch_Island_Platform():#지하철 상하행 알려주는 옵션
    global SearchListBox
    platform_box_Scrollbar = Scrollbar(window)
    platform_box_Scrollbar.pack()
    platform_box_Scrollbar.place(x=150, y=50)
    temp_font = font.Font(window, size=15, weight="bold", family="Consolas")
    SearchListBox = Listbox(window, font=temp_font, activestyle="none",width = 10, height = 1, borderwidth = 12, relief = "ridge",yscrollcommand = platform_box_Scrollbar.set)
    SearchListBox.insert(1, "상행")
    SearchListBox.insert(2, "하행")
    SearchListBox.insert(3, "상하행")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)
    platform_box_Scrollbar.config(command=SearchListBox.yview)

def Init_Search_Button_Action():
    global SearchListBox
    pass

def Init_Render_Text():
    render_text_scrollbar=Scrollbar(window)
    render_text_scrollbar.pack()
    render_text_scrollbar.place(x=375,y=200)
    tempfont=font.Font(window,size=10,family="Consolas")
    render_text=Text(window,width=49,height=27,borderwidth=12,relief="ridge",yscrollcommand=render_text_scrollbar.set)
    render_text.pack()
    render_text.place(x=10,y=215)
    render_text_scrollbar.config(commande=render_text.yview)
    render_text_scrollbar.pack(size=RIGHT,fill=BOTH)
    render_text.configure(stat="disabled")

def Sbway_Name_Search():
    global sbway_name_search,encoding,Line_four,start,root,begine_end_sbway, arvlMsg,current_position,present_door,division
    sbway_name = str(sbway_name_search.get())
    if(start==False):
        encoding = parse.quote(Line_four["정왕"])
    else:
        encoding = parse.quote(Line_four[sbway_name])
        Change_Text_Box()
    start=True


# GUI
def Change_Text_Box():
    global begine_end_sbway, arvlMsg,current_position,present_door,division
    for a in root.findall("row"):
        begine_end_sbway.configure(text=a.findtext("trainLineNm"))
        arvlMsg.configure(text=a.findtext("arvlMsg2"))
        current_position .configure(text=a.findtext("arvlMsg3"))
        present_door .configure(text=a.findtext("subwayHeading"))


start=False

window = Tk()
window.geometry("1000x1000")  # GUI 크기

API()
Init_Top_Text()
InitSearch_Island_Platform()
Init_Input_Label()
Init_Search_Button()
Init_Search_Button_Action()
Sbway_Name_Search()

for a in root.findall("row"):
    begine_end_sbway = Label(window, text=a.findtext("trainLineNm"))
    begine_end_sbway.pack()
    arvlMsg = Label(window, text=a.findtext("arvlMsg2"))
    arvlMsg.pack()
    current_position = Label(window, text=a.findtext("arvlMsg3"))
    current_position.pack()
    present_door = Label(window, text=a.findtext("subwayHeading"))
    present_door.pack()
    division = Label(window, text="----------------")
    division.pack()

window.mainloop()
