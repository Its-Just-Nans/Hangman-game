from turtle import *

# Pour nommer la fenêtre de jeu
title("Le jeu du pendu !")

tracer(0)

# Vitesse d'éxécution du dessin
speed("fast")
setup(600,600)

# Barre du sol
penup()
goto(-90,-250)
pendown()

width(10)
color("brown")

left(180)
fd(175)
right(180)

# Barre vertical
penup()
goto(-220,-250)
pendown()

width(10)
color("brown")

left(90)
fd(450)
right(90)

#petit tchitchou
penup()
goto(-160,-250)
pendown()

width(10)
color("brown")

left(128)
fd(90)

right(128)

#poutre du  haut
penup()
goto(-260,200)
pendown()

width(10)
color("brown")

left(0)
fd(400)

right(0)

#corde
penup()
goto(120,194)
pendown()

width(9)
color("orange")

left(-90)
fd(65)

right(-90)

penup()
goto(118,190)
pendown()

width(5)
color("black")

left(0)
fd(5)

right(0)

penup()
goto(118,175)
pendown()

width(5)
color("black")

left(0)
fd(5)

penup()
goto(118,160)
pendown()

width(5)
color("black")

left(0)
fd(5)

right(0)

penup()
goto(118,145)
pendown()

width(5)
color("black")

left(0)
fd(5)

right(0)

penup()
goto(118,130)
pendown()

width(5)
color("black")

left(0)
fd(5)

right(0)

#tête
penup()
goto(119,123)
pendown()

color("red")
right(90)
begin_fill()
circle(20)
end_fill()
left(90)

#corps
penup()
goto(118,117)
pendown()

width(10)
color("black")

left(-90)
fd(130)

right(-90)

#bras droit
penup()
goto(118,100)
pendown()

width(8)
color("black")

left(-80)
fd(75)

right(-80)

#bras gauche
penup()
goto(118,100)
pendown()

width(8)
color("black")

left(-70)
fd(70)

right(-70)

#jambe droite
penup()
goto(118,-13)
pendown()

width(8)
color("black")

left(-80)
fd(75)

right(-33)
fd(20)
right(-47)

#jambe gauche
penup()
goto(118,-13)
pendown()

width(8)
color("black")

left(-97)
fd(67)

right(-30)
fd(20)
right(-60)




#mot de fin
penup()
goto(-100,0)
pendown()

color("red")
write("PENDU !",font=("Arial", 24, "normal"))

input()
