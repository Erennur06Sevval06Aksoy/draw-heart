#Çizim için gerekli kütüphaneleri projeye eklemek
from turtle import *
#Çizim yapılacak rengi belirlemek
color("black")
#Çizimin başladıüını belirtmek
begin_fill()
#Çizim kalınlığını belirlemek
pensize(5)
#Sola verilen açı
left(50)
#kalbin çiziminin başlama noktasını belirlemek
forward(133)
#Kalbin sağ yarısının eğimini ayarlamak
circle(50,200)
#kalbin sol yarısının başlangıç noktasını belirlemek
right(140)
#Kalbin sol yarısının eğimini ayarlamak
circle(50,200)
#kalbin çiziminin bitiş noktasını belirlemek
forward(133)
#Kalbin içini doldurmak
end_fill()
