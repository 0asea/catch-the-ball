# Importam librariile
import turtle

# Variabilele

# Scorul jucatorului
p_score = 0
# Scorul compiuterului
ai_score = 0
# Pozitia verticala a paletei jucatorului
p_pos = 0
# Viteza platformei Ai
ai_speed = 0.13

# Ecranul jocului

# Cream variabila ferestrei in care se va desfasura joaca
s = turtle.Screen()
# Alegem culoarea la fonul din spate
s.bgcolor("black")
# Setam inaltimea si latimea ecranului
s.setup(width=800, height=600)
# Denumeste fereastra
s.title("Ping Pong")
"""
Argumentul 0 în s.tracer(0) înseamnă că actualizarea automată (in turtle) a ecranului este dezactivată. Aceasta este o tehnică frecvent folosită în jocurile simple create cu turtle pentru a îmbunătăți performanța și a evita actualizările repetitive ale ecranului. Atunci când actualizarea automată este dezactivată, modificările grafice sunt vizibile doar atunci când este apelată funcția s.update() sau când se cere actualizarea ecranului în alt mod.
"""
s.tracer(0)

# Cream scorul AI

# Cream variabila prntru marcherul ce deseneaza scorul AI
score_pen_ai = turtle.Turtle()
# Ridicam marcherul (ce se afla pe coordinatele 0,0)
score_pen_ai.penup()
score_pen_ai.setposition(-300, 275)
# Coboram marcerul jos
score_pen_ai.pendown()
# Selectam culoarea
score_pen_ai.color("green")
# Ascunde marcherul
score_pen_ai.hideturtle()
"""
1. Textul care trebuie afișat, include textul de care avem nevoie si vatiabila ai_score f"AI Score {ai_score}".
2. False: Acest argument controlează dacă sau nu să se deseneze o linie sub text. În acest caz, este setat la False, deci nu se va desena nicio linie sub text.
3. align="left": Acest argument specifică alinierea textului.
4. font=("Arial", 14, "normal"): Acest argument specifică fontul, dimensiunea și stilul textului.
"""
score_pen_ai.write(f"AI Score {ai_score}", False, align="left", font=("Arial", 14, "normal"))

# Cream scorul jucatorului (aceliasi etape ca mai sus)

# Turtle craza un marcher pe ecran pe ecran (ce dupa poate fi modificat)
score_pen = turtle.Turtle()
score_pen.penup()
score_pen.setposition(210, 275)
score_pen.pendown()
score_pen.color("green")
score_pen.hideturtle()
score_pen.write(f"Score {p_score}", False, align="left", font=("Arial", 14, "normal"))

# Cream variabila paletei jucatorului
p_p = turtle.Turtle()
"""
Alegem forma marcherului. Turtle (țestoasă): Acesta este obiectul principal și implicit în turtle. Este o țestoasă care poate fi deplasată și rotită pentru a desena linii și forme.

Arrows (sageti): Puteți crea obiecte în formă de săgeată, care pot fi direcționate pentru a indica anumite direcții.

Circle (Cercuri): Obiectele pot fi create ca cercuri sau discuri. Acestea sunt folosite adesea pentru a marca puncte sau pentru a crea efecte vizuale.

Triangles (triunghiuri): Puteți crea obiecte în formă de triunghiuride diferite forme.

Square (pătrate): Obiectele pot fi create ca pătrate.

Rectangle (Dreptunghiuri): Similar cu pătratele, puteți crea dreptunghiuri cu laturi de lungimi diferite.

Polygons (Poligoane): Puteți crea obiecte în formă de poligoane cu un număr variabil de laturi.

Custom Shapes (Obiecte personalizate): De asemenea, puteți să creați obiecte personalizate folosind turtle.register_shape(). Aceasta vă permite să importați imagini personalizate și să le utilizați ca forme pentru obiectele turtle.

Aceste forme pot fi utilizate pentru a desena diverse figuri și pentru a crea grafică interactivă în cadrul framework-ului turtle. Puteți alege forma potrivită pentru scopul dvs. specific și să o deplasați, să o rotiți și să o colorezi după cum doriți.
"""
p_p.shape("square")
""" Setam dimensiunile, mai exact, această instrucțiune ajustează dimensiunea obiectului turtle pe axele verticale și orizontale, stretch_wid=5 specifică cât de mult să fie întins obiectul în direcția verticală. În acest caz, obiectul va fi întins vertical ceea ce face ca înălțimea sa să fie de 5 ori mai mare decât forma sa originală.

stretch_len=1 specifică cât de mult să fie întins obiectul în direcția orizontală. Valoarea 1 înseamnă că obiectul nu este întins pe orizontală și păstrează lățimea sa originală.
"""
p_p.shapesize(stretch_wid=5, stretch_len=1)
p_p.color("green")
p_p.penup()
p_p.setposition(350, 0)

# Cream variabila paletei AI (aceliasi etape ca mai sus)
p_c = turtle.Turtle()
p_c.shape("square")
p_c.shapesize(stretch_wid=5, stretch_len=1)
p_c.color("green")
p_c.penup()
# Variabila.setposition(-350, 0): Plasează markerul în poziția (pe axa x, pe axa y) de pe ecran.
p_c.setposition(-350, 0)

# Cream mingea
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
"""
Variabila.goto(0, 0): Plasează markerul în poziția (pe axa x, pe axa y) de pe ecran.

Ambele metode, ball.goto(0, 0) și ball.setposition(0, 0), pot fi folosite pentru a plasa obiectul ball în aceeași poziție inițială la coordonatele (0, 0) pe ecran.Ambele metode sunt corecte și pot fi folosite pentru a seta poziția inițială a unui obiect turtle. Alegerea dintre ele depinde de preferința și stilul programatorului. De obicei, programatorii aleg metoda pe care o găsesc mai intuitivă sau mai ușor de citit în contextul lor specific de cod.
"""
ball.goto(0, 0)
"""
ball.dx = 0.15 și ball.dy = 0.15: Aceste linii setează valoarea dx (viteza deplasării pe axa x) și dy (viteza deplasării pe axa y) ale mingii. Mingea se va deplasa cu 0.15 unități pe axa x și totatatea pe axa y la fiecare actualizare a ecranului, ceea ce controlează viteza de mișcare a mingii.
"""
ball.dx = 0.15
ball.dy = 0.15


"""
def moveUp(): Definește o funcție numită moveUp() fără argumente.

global p_pos: Această linie indică că variabila p_pos este o variabilă globală, ceea ce înseamnă că poate fi accesată și modificată în afara funcției.

p_pos += 25: Această linie adaugă 25 la valoarea variabilei p_pos. Practic, mărește poziția jucătorului (sau a platformei) pe axa verticală cu 25 unități.

if p_pos > 250: Dacă poziția (p_pos) depășește 250, atunci această ramură a codului este executată.

p_pos = 250: În acest caz, poziția (p_pos) este setată la 250. Acest lucru poate fi o limită superioară pentru mișcarea jucătorului în sus, pentru a evita să iasă din ecran.

În rezumat, funcția moveUp() este concepută pentru a muta poziția jucătorului în sus pe axa verticală cu o anumită distanță (15 unități), dar are o limită superioară de 250 unități pentru a preveni ieșirea din ecran.
"""
def moveUp():
    global p_pos
    p_pos += 25
    if p_pos > 250:
        p_pos = 250


# Indeplineste acceiasi functie ca si definitia de mai sus numai ca blocheaza accesul in partea de jos
def moveDown():
    global p_pos
    p_pos -= 25
    if p_pos < -250:
        p_pos = -250


"""
Instrucțiunea s.listen() este utilizată în framework-ul turtle din Python pentru a aștepta evenimente de la tastatură. În particular, această instrucțiune face ca fereastra grafică să fie pregătită să primească intrări de la tastatură de la utilizator.

După ce apelați s.listen(), puteți utiliza metode precum s.onkeypress() pentru a atribui funcții sau acțiuni anumitor evenimente de tastatură. Aceasta vă permite să controlați obiectele turtle sau să răspundeți la intrările utilizatorului, cum ar fi să mutați un obiect sau să declanșați alte acțiuni în joc.
"""
s.listen()
# Leaga functia de butonul apasat de utilizator
s.onkeypress(moveUp, "Up")
s.onkeypress(moveDown, "Down")

try:
    while True:
        """   
        ball.xcor() - functia ce mentine coordonatele pe axa x
        
        ball.dx (delta x) - viteza cu care mingea se deplaseaza pe axa x
        
        ball.ycor() - functia ce mentine coordonatele pe axa y
        
        ball.dy (delta y) - viteza cu care mingea se deplaseaza pe axa y

        ball.xcor() + ball.dx: Această expresie calculează noua poziție pe axa x a mingii. ball.xcor() returnează poziția curentă a mingii pe axa x, iar ball.dx reprezintă viteza deplasării mingii pe axa x. Prin adunarea acestor două valori, se obține noua poziție pe axa x după o mișcare.
                
        ball.ycor() + ball.dy: Această expresie calculează noua poziție pe axa y a mingii. ball.ycor() returnează poziția curentă a mingii pe axa y, iar ball.dy reprezintă viteza deplasării mingii pe axa y. Prin adunarea acestor două valori, se obține noua poziție pe axa y după o mișcare.
        
        În esență, această linie de cod actualizează poziția mingii pe baza vitezelor sale pe axele x și y. Ea adaugă viteza deplasării (ball.dx și ball.dy) la poziția curentă a mingii pe fiecare iterație a buclei, ceea ce face ca mingea să se deplaseze în direcția și cu viteza specificate de aceste valori.
        """
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
            ai_score += 1
            # Sterge ultimul lucru ce am facut cu el
            score_pen_ai.undo()
            score_pen_ai.write(f"AI Score {ai_score}", False, align="left", font=("Arial", 14, "normal"))

        if ball.xcor() < -390:
            ball.setposition(0, 0)
            ball.dx *= -1
            p_score += 1
            score_pen.undo()
            score_pen.write(f"Score {p_score}", False, align="left", font=("Arial", 14, "normal"))

        # Miscarea automata a platformei calculatorului dupa minge.
        if ball.ycor() > p_c.ycor():
            p_c.sety(p_c.ycor() + ai_speed)

        if ball.ycor() < p_c.ycor():
            p_c.sety(p_c.ycor() - ai_speed)

        # Detectarea coliziunii dintre minge si ambele platforme
        
        """
        ball.xcor() < 350 și ball.xcor() > 340: Aceste două condiții verifică dacă poziția actuală a mingii pe axa x (ball.xcor()) este mai mică de 350 și mai mare de 340. Aceasta înseamnă că mingea trebuie să fie la o distanță mică spre marginea dreaptă a platformei jucătorului.

        ball.ycor() < p_p.ycor() + 50 și ball.ycor() > p_p.ycor() - 50: Aceste două condiții verifică dacă poziția actuală a mingii pe axa y (ball.ycor()) este între poziția de sus (p_p.ycor() + 50) și poziția de jos (p_p.ycor() - 50) a platformei jucătorului. Acest interval de 50 unități pe axa y înseamnă că mingea trebuie să fie înăuntrul platformei jucătorului în ceea ce privește coordonata y.

        În esență, această verificare condițională se activează atunci când mingea se află în proximitatea platformei jucătorului pe axele x și y. Acest lucru indică o potențială coliziune între mingea și platforma jucătorului. Dacă această condiție este îndeplinită, atunci unele acțiuni ar putea avea loc, cum ar fi schimbarea direcției mingii sau înregistrarea unui punct pentru jucătorul curent, în funcție de logica specifică a jocului.
        """
        if (
            ball.xcor() < 350
            and ball.xcor() > 340
            and ball.ycor() < p_p.ycor() + 50
            and ball.ycor() > p_p.ycor() - 50
        ):
            # Oglindeste lovitura pe axa x
            ball.setx(340)
            ball.dx *= -1
        
        if (
            ball.xcor() > -350
            and ball.xcor() < -340
            and ball.ycor() < p_c.ycor() + 50
            and ball.ycor() > p_c.ycor() - 50
        ):
            ball.setx(-340)
            ball.dx *= -1

        # Miscarea paddle player
        p_p.setposition(350, p_pos)
        s.update()
except:
    pass