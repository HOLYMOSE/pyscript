import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수     
=def button(*args):+  link = "https://open.spotify.com/yser/es52z9sd2vknvo42?si=Tk3gXLNFRNqEDthvTGCOBw&utm_source=copy-link" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["green", "black"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "Kim Gyu Won")
write("description", "16 years old")
write("button", "spotify profil")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "like": "camera1",
  "habit": "listening to music",
  "animal": "penguin",
  "want": "camera and leng"
}
information(informations)
