from datos import lista
import pygame
import json
lista_preguntas = lista
    
def opcion_a(contador_sub2):
 '''
 Crea una sublista de las opciones a.
 Recibe como parámetro contador_sub2, que es quien actua como un índice.
 Retorna la opción del índice del contador_sub2.
 '''
 sublista2 = []
 for preg in lista_preguntas:
   sublista2.append(preg['a'])
 if contador_sub2 <= len(sublista2): 
   return sublista2[contador_sub2]

def opcion_b(contador_sub3):
 '''
 Crea una sublista de las opciones b.
 Recibe como parámetro contador_sub3, que es quien actua como un índice.
 Retorna la opción del índice del contador_sub3.
 '''
 sublista3 = []
 for preg in lista_preguntas: 
   sublista3.append(preg['b'])
 if contador_sub3 <= len(sublista3):
  return sublista3[contador_sub3] 

def opcion_c(contador_sub4):
 '''
 Crea una sublista de las opciones d.
 Recibe como parámetro contador_sub4, que es quien actua como un índice.
 Retorna la opción del índice del contador_sub4.
 '''
 sublista4 = []
 for preg in lista_preguntas: 
   sublista4.append(preg['c'])
 if contador_sub4 <= len(sublista4):  
  return sublista4[contador_sub4]

def sublista_correctas(contador):
 '''
 Crea una sublista de las opciones correctas.
 Recibe como parámetro contador, que es quien actua como un índice.
 Retorna la opción del índice del contador.
 '''
 sublista_correcta = []
 for preg in lista_preguntas:
    sublista_correcta.append(preg['correcta'])
 if contador <= len(sublista_correcta):  
    return sublista_correcta[contador]

def contador_de_correcta(contador_correcta):
 '''
 Se suma a contador_correcta +1 cuando la función es llamada.
 Recibe como parámetro contador, que es quien actua como un índice.
 Retorna la opción del índice de contador_correcta.
 '''
 contador_correcta += 1
 return contador_correcta

def carga_datos():
  '''
  Carga los datos del archivo json.
  '''
  with open('data34.json', 'r') as file:
    data = json.load(file)
  return data
data1 = carga_datos()

def guardar_json(lista_info):
    '''
    Guarda la lista de jugadores con sus puntajes al archivo json.
    Recibe como parámetro lista_info.
    '''
    with open('data34.json', 'w') as file:
      json.dump(lista_info, file, indent=4, ensure_ascii= False)

def ordenar_mayor(lista_jugadores):
  '''
  Ordena de mayor a menor, según el puntaje, a cada jugador.
  Recibe como parámetro lista_jugadores.
  Retorna la lista ordenada
  '''
  for i in range(len(lista_jugadores) - 1):
    for j in range(i + 1, len(lista_jugadores)):
         if (lista_jugadores[i]["Score"] < lista_jugadores[j]["Score"]):
            # Intercambio
            aux = lista_jugadores[i]
            lista_jugadores[i] = lista_jugadores[j]
            lista_jugadores[j] = aux
 
  return lista_jugadores

def carga_datos2():
    '''
    Carga los datos del archivo json, etsa vez con los jugadores ordenados.
    '''
    with open('data34.json', 'r') as file:
     data = json.load(file)
    return data

def musica_juego(sonido_fondo_juego):
  '''
  Pone la musica solicitada.
  Recibe como parámetro sonido_fondo_juego, que es donde se encuentra la musica.
  '''
  pygame.mixer.init()
  pygame.mixer.music.set_volume(0.7)
  sonido_fondo_juego.set_volume(0.5)
  sonido_fondo_juego.play(-1)

def parar_musica_juego(sonido_fondo_juego):
  '''
  Detiene la musica.
  Recibe como parámetro sonido_fondo_juego, que es donde se encuentra la musica.
  '''
  sonido_fondo_juego.stop()

def musica1(sonido_fondo1):
  '''
  Pone la musica solicitada.
  Recibe como parámetro sonido_fondo1, que es donde se encuentra la musica.
  '''
  pygame.mixer.init()
  pygame.mixer.music.set_volume(0.7)
  sonido_fondo1.set_volume(0.5)
  sonido_fondo1.play()

def parar_musica1(sonido_fondo1):
  '''
  Detiene la musica.
  Recibe como parámetro sonido_fondo1, que es donde se encuentra la musica.
  '''
  sonido_fondo1.stop()

def musica2(sonido_fondo2):
  '''
  Pone la musica solicitada.
  Recibe como parámetro sonido_fondo2, que es donde se encuentra la musica.
  '''
  pygame.mixer.init()
  pygame.mixer.music.set_volume(0.7)
  sonido_fondo2.set_volume(0.5)
  sonido_fondo2.play()

def parar_musica2(sonido_fondo2):
  '''
  Detiene la musica.
  Recibe como parámetro sonido_fondo2, que es donde se encuentra la musica.
  '''
  sonido_fondo2.stop()

def musica3(sonido_fondo3):
  '''
  Pone la musica solicitada.
  Recibe como parámetro sonido_fondo3, que es donde se encuentra la musica.
  '''
  pygame.mixer.init()
  pygame.mixer.music.set_volume(0.7)
  sonido_fondo3.set_volume(0.5)
  sonido_fondo3.play()

def parar_musica3(sonido_fondo3):
  '''
  Detiene la musica.
  Recibe como parámetro sonido_fondo3, que es donde se encuentra la musica.
  '''
  sonido_fondo3.stop()

def musica4(sonido_fondo4):
  '''
  Pone la musica solicitada.
  Recibe como parámetro sonido_fondo4, que es donde se encuentra la musica.
  '''
  pygame.mixer.init()
  pygame.mixer.music.set_volume(0.7)
  sonido_fondo4.set_volume(0.5)
  sonido_fondo4.play()

def parar_musica4(sonido_fondo4):
  '''
  Detiene la musica.
  Recibe como parámetro sonido_fondo4, que es donde se encuentra la musica.
  '''
  sonido_fondo4.stop()