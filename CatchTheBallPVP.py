import turtle

# Scorul jucatorului nr. 1
p1_score = 0
# Scorul jucatorului nr. 2
p2_score = 0
# Pozitia paletei jucatorului nr.1
p1_pos = 0
# Pozitia paletei jucatorului nr.1
p2_pos = 0

s = turtle.Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Ping Pong PVP")
s.tracer(0)

score_pen1 = turtle.Turtle()
score_pen1.penup()
score_pen1.setposition(-300, 275)
score_pen1.pendown()
score_pen1.color("green")
score_pen1.hideturtle()
score_pen1.write(f"P1 score {p1_score}", False, align="left", font=("Arial", 14, "normal"))

score_pen2 = turtle.Turtle()
score_pen2.penup()
score_pen2.setposition(210, 275)
score_pen2.pendown()
score_pen2.color("green")
score_pen2.hideturtle()
score_pen2.write(f"P2 score {p2_score}", False, align="left", font=("Arial", 14, "normal"))

p1_p = turtle.Turtle()
p1_p.shape("square")
p1_p.shapesize(stretch_wid=5, stretch_len=1)
p1_p.color("green")
p1_p.penup()
p1_p.setposition(-350, 0)

p2_p = turtle.Turtle()
p2_p.shape("square")
p2_p.shapesize(stretch_wid=5, stretch_len=1)
p2_p.color("green")
p2_p.penup()
p2_p.setposition(350, 0)

# Cream mingea
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15


def P1moveUp():
    global p1_pos
    p1_pos += 25
    if p1_pos > 250:
        p1_pos = 250
        

def P1moveDown():
    global p1_pos
    p1_pos -= 25
    if p1_pos < -250:
        p1_pos = -250
        

def P2moveUp():
    global p2_pos
    p2_pos += 25
    if p2_pos > 250:
        p2_pos = 250
        

def P2moveDown():
    global p2_pos
    p2_pos -= 25
    if p2_pos < -250:
        p2_pos = -250
        
        
s.listen()
# Leaga functia de butonul apasat de utilizator
s.onkeypress(P1moveUp, "w")
s.onkeypress(P1moveDown, "s")

s.onkeypress(P2moveUp, "Up")
s.onkeypress(P2moveDown, "Down")

try:
    while True:
        ball.setposition(ball.xcor() + ball.dx, ball.ycor() + ball.dy)

        # Coliziunea dintre minje si marginile de sus/jos
        if ball.ycor() > 290:
            # Seteaza coordonatele doar pe axa y
            ball.sety(290)
            # Negam pentru ricosare (290 * -1 = -290, + * - = - si - * - = +)
            ball.dy *= -1
            
        # Facem invers
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Coliziunea dintre minge si laturile laterare
        if ball.xcor() > 390:
            ball.setposition(0, 0)
            # Oglindeste si adauga scor
            ball.dx *= -1
            p1_score += 1
            # Sterge ultimul lucru ce am facut cu el
            score_pen1.undo()
            score_pen1.write(f"P1 score {p1_score}", False, align="left", font=("Arial", 14, "normal"))

        if ball.xcor() < -390:
            ball.setposition(0, 0)
            ball.dx *= -1
            p2_score += 1
            score_pen2.undo()
            score_pen2.write(f"P2 score {p2_score}", False, align="left", font=("Arial", 14, "normal"))

        # Detectarea coliziunii dintre minge si ambele platforme
        if (
            ball.xcor() < 350
            and ball.xcor() > 340
            and ball.ycor() < p2_p.ycor() + 50
            and ball.ycor() > p2_p.ycor() - 50
        ):
            # Oglindeste lovitura pe axa x
            ball.setx(340)
            ball.dx *= -1
        
        if (
            ball.xcor() > -350
            and ball.xcor() < -340
            and ball.ycor() < p1_p.ycor() + 50
            and ball.ycor() > p1_p.ycor() - 50
        ):
            ball.setx(-340)
            ball.dx *= -1

        # Miscarea paddle player
        p1_p.setposition(-350, p1_pos)
        p2_p.setposition(350, p2_pos)
        s.update()
except:
    pass