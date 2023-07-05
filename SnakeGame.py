"""" 
47      Gerekli kütüphaneleri import ediyoruz
52-59   Kod içerisinde kullanılacak sabit değişkenlere değer atıyoruz
61      Snake classı oluşturup nesne tabanlı programla yöntemi ile class içersinde fonksiyon oluşturduk
63      Yılanın başlangıçtaki boyunu ayarlayan kodu yazdık
64      Yılanın gezdiği kordinatları listeleyeceğimiz bir boş liste açtık
65      Yılanın gövdesini oluşturan kareleri listeleyeceğimiz bir boş liste açtık
67-68   Yılanın toplam BODY_PARTS sayısı kadar [0,0] konumunu koordinatlar listesine ekleyen döngüyü oluşturduk 
70-72   Yılanın koordinatlar listesindeki koordinatlara göre kareler oluşturup kareler listesine ekleyen döngüyü oluşturduk
74      Food classı oluşturup nesne tabanlı programla yöntemi ile class içersinde fonksiyon oluşturduk
76-77   .randint(x,y) metodu sayesinde x ile y dahil olmak üzere bu iki değişken arasında bir sayı ürettik
79      x ile y değişkenini Food öğesine rastgele konum atamak için kullanıyoruz
81      Elde ettiğimiz koordinatlar ile rastgele yerlerde food öğesi oluşmasını sağladık
83      Oyun içindeki hareketleri ve olayları kontrol etmek amaçlı fonksiyon oluşturduk
84      Yılanımızın baş kısmının attığı her adımın kodinatlarını x ve y değerlerine atadık 
86-96   Daha aşağılarda göreceğimiz direction değişkeninin durumuna göre x ve y değerlerine matematiksel işlem uyguladık
88      Koordinatlar listesinine matematiksel işlemler yapılmış yeni koordinatları 0. sıradan ekledik
100     Yılanımız her yeni bir konuma geçiş yaptığında o konumda yeni bir kare oluşuran canvas metodunuz yazdık
102     Yeni oluşan her bir kareyi yılanın başı olarak kareler listesine ekledik
104-118 Yılanın baş kısmı için oluşturulan karenin konumları food öğesinin konumları ile eş değer ise SPEED ve score değerimizi arttıran ve üstüne gittiğimiz food öğesini silip yeni food öğesi oluşturan If kodunu yazdık
120-125 Sürekli oluşturduğumuz kareler eğer food öğesinin konumu ile uyuşmuyorsa arkadan gelen kareleri silen else kodunu oluşturduk 
127-128 Daha aşağılarda göreceğimiz check_collisions fonksiyonu True ise game_over fonksiyonunu komutunu çalıştıran If kodunu oluşturduk
129-130 check_collisions fonksiyonu False ise window.after(SPEED, next_turn, snake, food)  komutunu çalıştıran Else kodunu oluşturduk. window.after() belli sürede belli fonksiyonu sürekli çalıştıran method 
132     Yılanımızın döneceği yönü belirleyen kodların bulunduğu fonksiyonu oluşturduk ve nesne olarak new_direction oluşturduk
133-146 Daha sonra oluşturduğumuz direction değişkenini global yaparak erişim sağladık ve key hareketlerimize göre direction değerimizi değiştiren If/else kodunu yazdık
148-158 Snake objesinin koordinatlarını ve penceremizin koordinatlarını kullanarak yada snake objenin iki parçası aynı konuma denk geldiğinde oyunu sonlandıran kodu oluşturduk   
160-163 Canvas çerçevesi içerisindeki herşeyi silip sadece GAME OVER yazısı yazan fonksiyon
171     Pwenceremizin boyutunu x ve y axislerinde değiştirilip değiştirilemeyeceğini ayarlar
174     Labelde kullanılacak score değerimizi belirledik
175     Yılanın başlangıç yönünü belirledik
188     Açılan pencerenin genişlik bilgisini verir
189     Açılan pencerenin yükseklik bilgisini verir
190     Bilgisyarınızın ekranının genişlik bilgisini verir
191     Bilgisyarınızın ekranının yükseklik bilgisini verir
193     Penceremizi ortalamak için x ekseni değişkeni oluşturduk
194     Penceremizi ortalamak için y ekseni değişkeni oluşturduk
196     Pencereyenin boyutunu ve konumunu .format metodu ile ayarladık
198     Yön tuşlarında sol olana basarak direction değerimizi sol olarak değiştirdiğimiz lambda fonksiyonu
199     Yön tuşlarında sağ olana basarak direction değerimizi sağ olarak değiştirdiğimiz lambda fonksiyonu
200     Yön tuşlarında yukarı olana basarak direction değerimizi yukarı olarak değiştirdiğimiz lambda fonksiyonu
201     Yön tuşlarında aşağı olana basarak direction değerimizi aşağı olarak değiştirdiğimiz lambda fonksiyonu
203     Snake classımızı snake adlı bir değişkene atadık
204     Food classımızı food adlı bir değişkene atadık

tag özelliği öğeyi etiketlemek için kullanılır
"""""
from tkinter import *
import random
import time


GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BODY_PARTS = 1
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, int((GAME_WIDTH / SPACE_SIZE) - 1)) * SPACE_SIZE
        y = random.randint(0, int((GAME_WIDTH / SPACE_SIZE) - 1)) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tags="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        global SPEED

        score += 1

        SPEED -= 2

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    if new_direction == "right":
        if direction != "left":
            direction = new_direction
    if new_direction == "up":
        if direction != "down":
            direction = new_direction
    if new_direction == "down":
        if direction != "up":
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=("consolas",70), text="GAME OVER", fill="red", tags="game")

def Quit():
    window.quit()

window = Tk()

window.title("Snake Game")
window.resizable(False,False)


score = 0
direction = "down"

label = Label(window,text="Puan:{}".format(score),font=("consolas",40))
label.pack()

button = Button(window, text="QUIT",command=Quit,font=("consolas",15))
button.pack()

canvas = Canvas(window,bg=BACKGROUND_COLOR,width=GAME_WIDTH,height=GAME_HEIGHT)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2)-5)
y = int((screen_height/2) - (window_height/2)-55)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake,food)

window.mainloop()