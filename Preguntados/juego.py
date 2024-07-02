import pygame
from datos import lista
from biblioteca_juegos import *
import json


lista_preguntas = lista
pygame.init() #Se inicializa pygame
screen = pygame.display.set_mode([500, 500]) #Se crea una ventana
pygame.display.set_caption("Trivia")

tick = pygame.USEREVENT + 0
pygame.time.set_timer(tick, 10)

pixel_font = pygame.font.Font("Minecraft.ttf", 32)
pixel_font2 = pygame.font.Font("Minecraft.ttf", 32)
pixel_font3 = pygame.font.Font("game_over.ttf", 80)
font = pygame.font.SysFont("Arial Narrow", 50)
#font_empezar = pygame.font.SysFont("Arial Narrow", 40)
font40 = pygame.font.SysFont("Arial Narrow", 40)
font30 = pygame.font.SysFont("Arial Narrow", 30)
font39 = pygame.font.SysFont("Arial Narrow", 39)
font23 = pygame.font.SysFont("Arial Narrow", 23)
text_start = pixel_font.render("Empezar", True, (255, 255, 255))
text_ver_puntaje = pixel_font2.render("Ver puntaje", True, (255, 255, 255))
text_salir = pixel_font.render("Salir", True, (255, 255, 255))
text_volver = pixel_font.render("Volver", True, (255, 255, 255))
text_pregunta = font40.render("Pregunta", True, (255, 255, 255))
text_reiniciar = font30.render("Reiniciar", True, (255, 255, 255))
text_conclusion1 = pixel_font3.render("SIGUE INTENTANDOLO", True, (199, 17, 17))
text_conclusion2 = pixel_font3.render("¡FELICITACIONES!", True, (199, 17, 17))
text_aviso1 = font30.render("Menos de 50:", True, (151, 151, 151))
text_aviso2 = font30.render("Entre 50 y 80 puntos:", True, (151, 151, 151))
text_aviso3 = font30.render("Entre 80 y 140 puntos:", True, (151, 151, 151))
text_aviso4 = font30.render("Más de 140 puntos:", True, (151, 151, 151))


rect_boton_jugar = pygame.Rect(157, 216, 180, 43)
rect_boton_pregunta = pygame.Rect(170, 400, 170, 60)
rect_boton_reiniciar = pygame.Rect(196, 340, 120, 50)
rect_boton_sub2 = pygame.Rect(10, 215, 125, 35)
rect_boton_sub3 = pygame.Rect(184, 215, 125, 35)
rect_boton_sub4 = pygame.Rect(343, 215, 138, 35)
rect_boton_ver_puntajes = pygame.Rect(156, 269, 190, 55)
rect_boton_volver = pygame.Rect(180, 455, 140, 42)
rect_boton_salir = pygame.Rect(162, 330, 175, 43)


imagen_inicio = pygame.image.load("trivia.png")
imagen_inicio = pygame.transform.scale(imagen_inicio, (500, 500))

imagen_menu = pygame.image.load("trivia_menu.png")
imagen_menu = pygame.transform.scale(imagen_menu, (500, 500))

imagen_fondo = pygame.image.load("fondo_juego.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (500, 500))

imagen_podio = pygame.image.load("podio.png")
imagen_podio = pygame.transform.scale(imagen_podio, (500, 500))

imagen_icono = pygame.image.load("icono.png")
imagen_icono = pygame.transform.scale(imagen_icono, (180, 180))

imagen_estrella = pygame.image.load("estrella.png")
imagen_estrella = pygame.transform.scale(imagen_estrella, (20, 20))

imagen_estrella2 = pygame.image.load("estrella.png")
imagen_estrella2 = pygame.transform.scale(imagen_estrella2, (25, 25))

imagen_final = pygame.image.load("escenariopuntaje2.png")
imagen_final = pygame.transform.scale(imagen_final, (500, 500))

pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("intro.wav")
sonido_fondo.set_volume(0.5)
sonido_fondo.play()

sublista = []
for i in lista_preguntas:
    sublista.append(i['pregunta'])
contador = 0
'''
sublista2 = []
for preg in lista_preguntas:
 sublista2.append(preg['a'])
sublista3 = []
for preg in lista_preguntas: 
 sublista3.append(preg['b'])
sublista4 = []
for preg in lista_preguntas: 
 sublista4.append(preg['c'])
'''
contador_a = 0
contador_b = 0
contador_c = 0
contador_score = 0
contador_correcta = 0
contador_op = 0
contador_tiempo = 0

sonido_fondo1 = pygame.mixer.Sound("stars1.wav")
sonido_fondo2 = pygame.mixer.Sound("stars2.wav")
sonido_fondo3 = pygame.mixer.Sound("stars3.wav")
sonido_fondo4 = pygame.mixer.Sound("stars4.wav")
sonido_fondo_juego = pygame.mixer.Sound("musica_juego.wav")

text_nombre = ''
mostrar = True
pantalla_b = False
pantalla_c = False
pantalla_actual = "a"
iniciar_musica = False
iniciar_musica2 = False
mostrar_pregunta = False
running = True
#screen.fill((0, 0, 153)) # Se pinta el fondo de la ventana   
while running:
   # Se verifica si el usuario cerro la ventana
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       contador_tiempo += 1
       if contador_tiempo == 400:
           mostrar = False
          

       if mostrar == True:
         screen.blit(imagen_inicio, (0, 0))
       else:
         if event.type == pygame.MOUSEBUTTONDOWN:
          if rect_boton_jugar.collidepoint(event.pos):
           pantalla_actual = "b"
           pantalla_b = True
           pantalla_c = True
          if pantalla_b == True:
           if contador >= len(sublista) -1: 
             pantalla_actual = "c"
             if iniciar_musica == False and contador_score <= 50:
               iniciar_musica = True
               musica1(sonido_fondo1)
             if iniciar_musica == False and contador_score > 50 and contador_score <= 80:
               musica2(sonido_fondo2)
               iniciar_musica = True
             elif iniciar_musica == False and contador_score > 80 and contador_score <= 140:
              musica3(sonido_fondo3)
              iniciar_musica = True
             elif iniciar_musica == False and contador_score > 140:
              musica4(sonido_fondo4)
              iniciar_musica = True
           if pantalla_c == True:
             if iniciar_musica2 == False:
               musica_juego(sonido_fondo_juego)
               iniciar_musica2 = True
             if rect_boton_sub2.collidepoint(event.pos):   
              sublista_correcta = sublista_correctas(contador_correcta)    
              print(sublista_correcta)
              if sublista_correcta == "a":
               contador += 1
               contador_a += 1
               contador_b += 1
               contador_c += 1
               contador_correcta = contador_de_correcta(contador_correcta)
               contador_op = 0
               contador_score += 10 
              else:
                contador_op += 1
             if rect_boton_sub3.collidepoint(event.pos):   
              sublista_correcta = sublista_correctas(contador_correcta)   
              print(sublista_correcta)
              if sublista_correcta == "b":
               contador += 1
               contador_a += 1
               contador_b += 1
               contador_c += 1
               contador_correcta = contador_de_correcta(contador_correcta)
               contador_op = 0
               contador_score += 10
              else:
                contador_op += 1
             if rect_boton_sub4.collidepoint(event.pos):   
              sublista_correcta = sublista_correctas(contador_correcta)    
              print(sublista_correcta)
              if sublista_correcta == "c":
               contador += 1
               contador_a += 1
               contador_b += 1
               contador_c += 1
               contador_correcta = contador_de_correcta(contador_correcta)
               contador_op = 0
               contador_score += 10   
              else:
                contador_op += 1
             if rect_boton_reiniciar.collidepoint(event.pos):
              contador = 0
              contador_a = 0
              contador_b = 0
              contador_c = 0
              contador_correcta = 0
              contador_score = 0
              contador_op = 0
             if contador_op >= 2: 
              contador += 1
              contador_a += 1
              contador_b += 1
              contador_c += 1
              contador_correcta += 1 
              contador_op = 0
 

         
         if pantalla_actual == "a":
           screen.blit(imagen_menu, (0, 0))  # Se pinta el fondo de la ventana
           pygame.draw.rect(screen, (62, 145, 200), rect_boton_jugar, border_radius=15)
           screen.blit(text_start, (180, 225))
           pygame.draw.rect(screen, (62, 145, 200), rect_boton_ver_puntajes, border_radius=15)
           screen.blit(text_ver_puntaje, (157, 283))
           pygame.draw.rect(screen, (62, 145, 200), rect_boton_salir, border_radius=15)
           screen.blit(text_salir, (218, 338))
           if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_boton_salir.collidepoint(event.pos):
             running = False
            if rect_boton_ver_puntajes.collidepoint(event.pos):
             pantalla_actual = "d" 
         if pantalla_actual == "b":
           screen.blit(imagen_fondo, (0, 0))
           screen.blit(imagen_estrella, (275, 25))
           screen.blit(imagen_estrella, (353, 45))
           screen.blit(imagen_estrella, (373, 45))
           screen.blit(imagen_estrella, (367, 65))
           screen.blit(imagen_estrella, (387, 65))
           screen.blit(imagen_estrella, (407, 65))
           screen.blit(imagen_estrella, (335, 85))
           screen.blit(imagen_estrella, (355, 85))
           screen.blit(imagen_estrella, (375, 85))
           screen.blit(imagen_estrella, (395, 85))
           screen.blit(text_aviso1, (146, 25))
           screen.blit(text_aviso2, (146, 45))
           screen.blit(text_aviso3, (146, 65))
           screen.blit(text_aviso4, (146, 85))
           pygame.draw.rect(screen, (254, 184, 51), rect_boton_pregunta, border_radius=15)
           pygame.draw.rect(screen, (254, 184, 51), rect_boton_reiniciar, border_radius=15)
           pygame.draw.rect(screen, (254, 184, 51), rect_boton_sub2, border_radius=15)
           pygame.draw.rect(screen, (254, 184, 51), rect_boton_sub3, border_radius=15)
           pygame.draw.rect(screen, (254, 184, 51), rect_boton_sub4, border_radius=15)
           if mostrar_pregunta == False:
             if event.type == pygame.MOUSEBUTTONDOWN:
              if rect_boton_pregunta.collidepoint(event.pos):
               mostrar_pregunta = True
           else:
             rect_boton_pregoy2 = pygame.Rect(170, 400, 170, 60)
             pygame.draw.rect(screen, (254, 184, 51), rect_boton_pregoy2, border_radius=15)
             if event.type == pygame.MOUSEBUTTONDOWN:
              if rect_boton_pregoy2.collidepoint(event.pos):
               sublista_correcta = sublista_correctas(contador_correcta)
               #print(sub)
               contador +=1
               sub2 = opcion_a(contador_a)
               contador_a += 1
               sub3 = opcion_b(contador_b)
               contador_b += 1
               sub4 = opcion_c(contador_c)
               contador_c += 1
               contador_correcta = contador_de_correcta(contador_correcta)  
               contador_op = 0
               #contador_correcta += 1
               print(sub2)
               print(sub3)
               print(sub4) 
           screen.blit(text_pregunta, (196, 418))
           screen.blit(text_reiniciar, (212, 357))
           text_puntaje = font30.render(f"Score: {contador_score}", True, (0, 0, 0))
           screen.blit(text_puntaje, (10, 260))
           if mostrar_pregunta == True:
            sub = sublista[contador]
            text_preguntas = font23.render(sub, True, (0, 0, 0))
            screen.blit(text_preguntas, (9, 155))
            sub2 = opcion_a(contador_a)
            text_sublista2 = font23.render(sub2, True, (255, 255, 255))
            screen.blit(text_sublista2, (19, 225))
            sub3 = opcion_b(contador_b)
            text_sublista3 = font23.render(sub3, True, (255, 255, 255))
            screen.blit(text_sublista3, (189, 225))
            sub4 = opcion_c(contador_c)
            text_sublista4 = font23.render(sub4, True, (255, 255, 255))
            screen.blit(text_sublista4, (349, 225))
           screen.blit(imagen_icono, (-19, -17))
         if pantalla_actual == "c":
           parar_musica_juego(sonido_fondo_juego)
           pantalla_c = False
           screen.blit(imagen_final, (0, 0))
           guardar_info = []
           data1 = carga_datos()
           if contador_score <= 50:
             screen.blit(text_conclusion1, (80, 350))
             text_puntaje_final = font39.render(f"Score: {contador_score}", True, (0, 0, 0))
             screen.blit(text_puntaje_final, (145, 220))
             text_estrella = font39.render("Estrellas:", True, (0, 0, 0))
             screen.blit(text_estrella, (145, 160))
             screen.blit(imagen_estrella2, (263, 160))
             if event.type == pygame.KEYDOWN:
              text_nombre += event.unicode              
              if event.key == pygame.K_RETURN:
                parar_musica1(sonido_fondo1)
                if len(text_nombre) > 0:
                 text_nombre = text_nombre[:-1]
                for jugador in data1:
                  guardar_info.append({'Nombre': jugador['Nombre'], 'Score': jugador['Score']})
                guardar_info.append({'Nombre': text_nombre, 'Score': contador_score})
                ordenar_mayor(guardar_info)
                guardar_json(guardar_info)
                pantalla_actual = "a"
                pantalla_b = False
                print("Se presionó Enter")
             text_surface = font39.render(f"Nombre: {text_nombre}", True, (0, 0, 0))
             screen.blit(text_surface, (145, 280))
           elif contador_score > 50 and contador_score <= 80:
             screen.blit(text_conclusion2, (120, 350))
             text_puntaje_final = font39.render(f"Score: {contador_score}", True, (0, 0, 0))
             screen.blit(text_puntaje_final, (145, 225))
             text_estrella = font39.render("Estrellas:", True, (0, 0, 0))
             screen.blit(text_estrella, (145, 160))
             screen.blit(imagen_estrella2, (263, 160))
             screen.blit(imagen_estrella2, (283, 160))
             if event.type == pygame.KEYDOWN:
              text_nombre += event.unicode              
              if event.key == pygame.K_RETURN:
                parar_musica2(sonido_fondo2)
                if len(text_nombre) > 0:
                 text_nombre = text_nombre[:-1]
                for jugador in data1:
                  guardar_info.append({'Nombre': jugador['Nombre'], 'Score': jugador['Score']})
                guardar_info.append({'Nombre': text_nombre, 'Score': contador_score})
                ordenar_mayor(guardar_info)
                guardar_json(guardar_info)
                pantalla_actual = "a"
                pantalla_b = False
                print("Se presionó Enter")
             text_surface = font39.render(f"Nombre: {text_nombre}", True, (0, 0, 0))
             screen.blit(text_surface, (145, 280))
           elif contador_score > 80 and contador_score <= 140:
             screen.blit(text_conclusion2, (120, 350))
             text_puntaje_final = font39.render(f"Score: {contador_score}", True, (0, 0, 0))
             screen.blit(text_puntaje_final, (145, 225))
             text_estrella = font39.render("Estrellas:", True, (0, 0, 0))
             screen.blit(text_estrella, (145, 160))
             screen.blit(imagen_estrella2, (263, 160))
             screen.blit(imagen_estrella2, (283, 160))
             screen.blit(imagen_estrella2, (303, 160))
             if event.type == pygame.KEYDOWN:
              text_nombre += event.unicode              
              if event.key == pygame.K_RETURN:
                parar_musica3(sonido_fondo3)
                if len(text_nombre) > 0:
                 text_nombre = text_nombre[:-1]
                for jugador in data1:
                  guardar_info.append({'Nombre': jugador['Nombre'], 'Score': jugador['Score']})
                guardar_info.append({'Nombre': text_nombre, 'Score': contador_score})
                ordenar_mayor(guardar_info)
                guardar_json(guardar_info)
                pantalla_actual = "a"
                pantalla_b = False
                print("Se presionó Enter")
             text_surface = font39.render(f"Nombre: {text_nombre}", True, (0, 0, 0))
             screen.blit(text_surface, (145, 280))
           elif contador_score > 140:
             screen.blit(text_conclusion2, (120, 350))
             text_puntaje_final = font39.render(f"Score: {contador_score}", True, (0, 0, 0))
             screen.blit(text_puntaje_final, (145, 220))
             text_estrella = font39.render("Estrellas:", True, (0, 0, 0))
             screen.blit(text_estrella, (145, 160))
             screen.blit(imagen_estrella2, (263, 160))
             screen.blit(imagen_estrella2, (283, 160))
             screen.blit(imagen_estrella2, (303, 160))
             screen.blit(imagen_estrella2, (323, 160))
             if event.type == pygame.KEYDOWN:
              text_nombre += event.unicode              
              if event.key == pygame.K_RETURN:
                parar_musica4(sonido_fondo4)
                if len(text_nombre) > 0:
                 text_nombre = text_nombre[:-1]
                for jugador in data1:
                  guardar_info.append({'Nombre': jugador['Nombre'], 'Score': jugador['Score']})
                guardar_info.append({'Nombre': text_nombre, 'Score': contador_score})
                ordenar_mayor(guardar_info)
                guardar_json(guardar_info)
                pantalla_actual = "a"
                pantalla_b = False
                print("Se presionó Enter")
             text_surface = font39.render(f"Nombre: {text_nombre}", True, (0, 0, 0))
             screen.blit(text_surface, (145, 280))
         if pantalla_actual == "d":
           screen.blit(imagen_podio, (0, 0))
           pygame.draw.rect(screen, (184, 175, 148), rect_boton_volver, border_radius=15)
           screen.blit(text_volver, (200, 465))
           if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_boton_volver.collidepoint(event.pos):
             pantalla_actual = "a"
           #data2 = carga_datos2()
           data2 = carga_datos2()[0]
           retorno = ""  
           retorno += f"Nombre: {data2['Nombre']} | Score: {data2['Score']}"
           text_dat = font23.render(retorno, True, (0, 0, 0))  # Renderiza la pregunta actual

           data3 = carga_datos2()[1]
           retorno3 = ""  
           retorno3 += f"Nombre: {data3['Nombre']} | Score: {data3['Score']}"
           text_dat2 = font23.render(retorno3, True, (0, 0, 0))  # Renderiza la pregunta actual
           
           data4 = carga_datos2()[2]
           retorno4 = ""
           retorno4 += f"Nombre: {data4['Nombre']} | Score: {data4['Score']}"
           text_dat4 = font23.render(retorno4, True, (0, 0, 0))  # Renderiza la pregunta actual
           
           if data2['Score'] >= data3['Score'] and data2['Score'] >= data4['Score']:
             screen.blit(text_dat, (170, 5))
           elif data2['Score'] >= data3['Score'] and data2['Score'] <= data4['Score']:
             screen.blit(text_dat, (170, 5))
           elif data2['Score'] <= data3['Score'] and data2['Score'] >= data4['Score']:
             screen.blit(text_dat, (170, 5))
           elif data2['Score'] <= data3['Score'] and data2['Score'] <= data4['Score']:
             screen.blit(text_dat, (170, 5))

           if data3['Score'] >= data2['Score'] and data3['Score'] >= data4['Score']:
             screen.blit(text_dat2, (5, 140))
           elif data3['Score'] >= data2['Score'] and data3['Score'] <= data4['Score']:
             screen.blit(text_dat2, (5, 140))
           elif data3['Score'] <= data2['Score'] and data3['Score'] >= data4['Score']:
             screen.blit(text_dat2, (5, 140))
           elif data3['Score'] <= data2['Score'] and data3['Score'] <= data4['Score']:
             screen.blit(text_dat2, (5, 140))
            
           if data4['Score'] >= data2['Score'] and data4['Score'] >= data3['Score']:
             screen.blit(text_dat4, (290, 140))
           elif data4['Score'] >= data2['Score'] and data4['Score'] <= data3['Score']:
             screen.blit(text_dat4, (290, 140))
           elif data4['Score'] <= data2['Score'] and data4['Score'] >= data3['Score']:
             screen.blit(text_dat4, (290, 140))
           elif data4['Score'] <= data2['Score'] and data4['Score'] <= data3['Score']:
             screen.blit(text_dat4, (290, 140))
           #print(retorno)
           #text_puntajes = font.render(retorno, True, (0, 255, 0))
           #screen.blit(text_puntajes, (9, 225))

   pygame.display.flip()# Muestra los cambios en  la pantalla
pygame.quit() # Fin