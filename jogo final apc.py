import pyxel
from random import randint
from math import sqrt
pyxel.init(256, 256,fps=60)
pyxel.load("my_resource.pyxres")

x1=128
y1=200
x5=128
y5=128
x2=x1
y2=y1
contador_timer = 60
pontos = 0
i =0
numero_inimigos = 3
p = 0
o = 0

cooldown_contador=0
cooldown_laser_alert = 30
cooldown = 0
cooldown_laser=120

game_start=False
end_game=False

lista_x_inimigo=[]
lista_y_inimigo=[]
lista_x_laser=[]
lista_y_laser=[]
    
#coordenada inimigo
i =0
numero_inimigos = 2
for j in range (0,numero_inimigos):
    
    lista_x_inimigo.append(randint(0,256))
    lista_y_inimigo.append(randint(0,150))

#coordenada laser
numero_lasers=4
for t in range (0,numero_lasers):
    
    lista_x_laser.append(randint(0,256))
    lista_y_laser.append(randint(0,256))

def update():
    global x1, y1,x2,y2,x5,y5,cooldown_contador,game_start,COR,end_game,contador_timer,pontos, p, numero_lasers, o
    global cooldown_laser_alert,cooldown,cooldown_laser, i,movimento,j,numero_inimigos, lista_x_inimigo,lista_y_inimigo, f,t,lista_x_laser,lista_y_laser

    #menu
    if game_start == False :
        if pyxel.btnp(pyxel.KEY_RETURN):
            game_start = True 
        if cooldown_contador == 0 :
            cooldown_contador = 30
            COR = randint(1,15)
        elif cooldown_contador > 0 :
            cooldown_contador -= 1
    
    #Movimento
    if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    if end_game == False:
        
        if pyxel.btn(pyxel.KEY_W) and y1>0:
            y1-=2
        if pyxel.btn(pyxel.KEY_S) and y1<256:
            y1+=2
        if pyxel.btn(pyxel.KEY_A)  and x1>0:
            x1-=2
        if pyxel.btn(pyxel.KEY_D) and x1<256:
            x1+=2
      
    #aumeta numero de inimigos
    if contador_timer == 30:
        p += 8
        if p % 10 == 0:
            lista_x_inimigo.append(randint(0,256))
            lista_y_inimigo.append(randint(0,50))
            numero_inimigos += 1

    #aumeta numero de lasers
    if contador_timer == 30:
        o += 3
        if o % 10 == 0:
            lista_x_laser.append(randint(0,256))
            lista_y_laser.append(randint(0,50))
            numero_lasers += 1

    #movimento inimigo
    if end_game == False:
        for i in range(0 , numero_inimigos): 
            movimento = randint(1,4)
            if movimento==1:
                if lista_x_inimigo[i] < 256:
                   for f in range (1,4):
                       lista_x_inimigo[i]+=1
            if movimento==2:
                if lista_x_inimigo[i] > 0:
                   for f in range (1,4):
                       lista_x_inimigo[i]-=1
            if movimento==3:
                if lista_y_inimigo[i] < 256:
                    for f in range (1,4):
                       lista_y_inimigo[i]+=1
            if movimento==4:
                if lista_y_inimigo[i] > 0:
                    for f in range (1,4):
                       lista_y_inimigo[i]-=1
            

    #restart
    if pyxel.btnp(pyxel.KEY_R):
        end_game = False
        x1=128
        y1=200
        x5=128
        y5=128
        contador_timer = 60
        pontos = 0
        cooldown = 0
        numero_inimigos = 3
        numero_lasers = 4
        lista_y_laser = []
        lista_x_laser = []
        lista_x_inimigo = []
        lista_y_inimigo = []
        
        
        
        for j in range (0,numero_inimigos):
            lista_x_inimigo.append(randint(0,256))
            lista_y_inimigo.append(randint(0,150))
        for t in range (0,numero_lasers):
            lista_x_laser.append(randint(0,256))
            lista_y_laser.append(randint(0,256))
        

    #Timer
    if game_start == True and end_game==False:
        contador_timer -= 1
        if contador_timer == 0:
            contador_timer = 60
            pontos +=10
        
   
    #cooldowns
        
    if game_start == True and end_game == False:
        cooldown_laser_alert -= 1
        if cooldown_laser_alert == -30:
            cooldown_laser_alert = 30
            if cooldown != 3:
                cooldown+=1
        if cooldown == 3:
            cooldown_laser -=1
            if cooldown_laser == 0 :
                cooldown=0
                cooldown_laser=120
                lista_x_laser=[]
                lista_y_laser=[]
                for t in range (0,numero_lasers):
    
                    lista_x_laser.append(randint(0,256))
                    lista_y_laser.append(randint(0,256))

    #colisao com laser
    if pyxel.pget(x1-5,y1) == 8 or pyxel.pget(x1+5,y1) == 8 or pyxel.pget(x1,y1+5) == 8 or pyxel.pget(x1,y1-5) == 8:
        end_game = True

def draw():
    pyxel.cls(0)
    #Menu
    if game_start == False :
        pyxel.text (10, 10, "aperte enter para iniciar", pyxel.COLOR_WHITE)   
        pyxel.text (10, 40, "TUTORIAL:", pyxel.COLOR_WHITE)   
        pyxel.text (20, 50, "Use WASD para se movimentar", pyxel.COLOR_WHITE)   
        pyxel.text (20, 60, "Pressione R para reiniciar", pyxel.COLOR_WHITE)
        pyxel.text (20, 70, "Use Q para fechar o aplicativo", pyxel.COLOR_WHITE)  
        pyxel.rectb(0, 192, 256, 64, 7)
        pyxel.text (10, 215, "TRABALHO FINAL DE APC", pyxel.COLOR_WHITE)
        pyxel.text (10, 230, "DESENVOLVEDOR: Christian Hirsch Santos", COR)
        pyxel.text (10, 240, "DESENVOLVEDOR: Vitor Bellucci de Carvalho", COR)

    #Objetos
    if game_start == True:
        pyxel.blt(x1-4, y1-4, img=0, u=0, v=0, w=9, h=9, colkey=0)
        for x_inimigo,y_inimigo in zip (lista_x_inimigo,lista_y_inimigo):
            pyxel.blt(x_inimigo-8, y_inimigo-7, img=0, u=0, v=8, w=14, h=14, colkey=0)
    
    pyxel.text (10, 30, "{0}".format(pontos), pyxel.COLOR_WHITE)

    #Fim de jogo 

    if end_game == True: 
        pyxel.text (10, 50, "Voce morreu !", pyxel.COLOR_DARK_BLUE)
        pyxel.text (10, 60, "Pressione R para reiniciar", pyxel.COLOR_DARK_BLUE)

#cenario 1
    if cooldown != 3 :

        if cooldown_laser_alert < 1:
            for x_laser,y_laser in zip (lista_x_laser,lista_y_laser):
                pyxel.rectb(x_laser, 0, 4, 256, 7)
                pyxel.rectb(0, y_laser, 256, 4, 7)
    
    if cooldown == 3 :
        if cooldown_laser !=0 :
            for x_laser,y_laser in zip (lista_x_laser,lista_y_laser):
                pyxel.rect(x_laser, 0, 4, 256, 8)
                pyxel.rect(0, y_laser, 256, 4, 8)

pyxel.run(update, draw)