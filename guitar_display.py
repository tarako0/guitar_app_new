import guitar
a=guitar.Guitar(0)
#Dキーの指板座標と度数取得
for i, j in a.display_scale()[1].items():
    print(i,j)
