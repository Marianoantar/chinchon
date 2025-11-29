'''
Modulo System
'''

# Importaciones
from deck import *
from players import *
from evaluador import *

# ---------------------
# repartir_cartas()
# ---------------------
def repartir_cartas(
    jugadores: dict[str,list[list[tuple[int,str]],int,bool]], 
    mazo:list[tuple[int,str]],
    descarte: list[tuple[int,str]]
    ):
    ''' 
    Reparte 7 cartas del mazo a cada participante, dando una carta a cada uno
    hasta llegar a las 7 por cada jugador.
    Entra: jugadores, mazo, descarte
    Sale:
    Nota entra descarte ya que si mazo se queda sin cartas acude a el
    '''
    # Itera jugadores
    for cant in range(7):
        for jugador in jugadores:
            if len(mazo) == 0: 
                # Si el Mazo se queda sin cartas generar otro del descarte
                print(
                    "*" * 20 +
                    "\n El mazo quedó sin cartas\n Mezclando y generando mazo del descarte\n" +
                    "*" * 20 
                    ) 
                rearmar_mazo_del_descarte(mazo, descarte)
            
            # Robar carta del mazo
            carta = robar_carta_mazo(mazo)
            
            # Jugador recibe la carta
            # Se agrega a la mano
            jugadores[jugador][0].append(carta)
        
            # Se agrega a libres
            jugadores[jugador][2].append(carta)

# ---------------------
# mostrar Encabezado
# ---------------------
def mostrar_encabezado_turno(jugador):
    '''
    Funcion que muestra encabezado del turno con numbre del jugador
    '''
    print()
    print('*' * 41)
    print(f'       SIGUIENTE TURNO - {jugador}')
    print('*' * 41)
    
# ---------------------
# cortar()
# ---------------------
def cortar(nombre, jugadores):
    '''
    Funcion que inicia proceso de corte
    Entra: nombre del jugador que corta y jugadores(dict)
    '''
    print(f"\n***** Iniciando Proceso de Corte de {nombre} *****\n")
    
    # Recorrer Jugadores
    for jugador in jugadores:
        pass


# ---------------------
# comienzo_juego () COMIENZO DE PARTIDA!!!!
# ---------------------
def comienzo_juego(
    jugadores: dict[int,list[str, int, bool]],
    mazo: list[tuple[int,str]], 
    descarte: list[tuple[int,str]] 
    ):
    
    '''
    Funcion que comienza el Juego Chinchon
    Ingresan: 
        -jugadores, 
        -mazo, 
        -descarte
    
    '''
    
    print("\n************** COMIENZO DE JUEGO **************\n")
    
    mostrar_cartas(jugadores)
    
    print("\nCarta visible en pila de descarte: ",descarte[-1])
    print("Cantidad de cartas en descarte: ", len(descarte))
    
    print("Cantidad de cartas en el mazo: ", len(mazo))
    
    # COMIENZO DE RONDAS
    
    while sum(1 for jugador in jugadores if jugadores[jugador][4]) > 1: # Repite ciclo de Rondas hasta que quede 1 jugador
    
        # COMIENZO DE TURNOS
        corte = False
        while not corte:
            for jugador in jugadores:
                # Encabezado
                mostrar_encabezado_turno(jugador)
                
                # ANALIZAR CARTAS
                analizar(jugador = jugadores[jugador])
                
                datos_jugador = jugadores[jugador]
                mostrar_cartas_mano(jugador, datos_jugador)
                
                # Levantar carta
                while True:
                    carta = levantar_carta(mazo, descarte)
                    # Chequear carta
                    if carta == None:
                        rearmar_mazo_del_descarte(mazo, descarte)
                        continue
                    
                    # Tengo carta levantada
                    print(f"\n  .Carta levantada: {carta}\n")
                    break  
                
                recibir_carta(jugadores[jugador], carta)
                
                # ANALIZAR CARTAS
                analizar(jugador = jugadores[jugador])
                
                # Mostrar cartas en mano
                mostrar_cartas_mano(jugador, jugadores[jugador])
                
                # Se puede cortar ???
                puede_cortar, carta_corte = analizar_cortar(datos_jugador[2])
                if puede_cortar:
                    
                    # PUEDE CORTAR
                    print(f"\n¡¡¡¡¡¡ {jugador} ya puede cortar !!!!!\n")
                    desicion =  input(f"Quiere cortar(1) o seguir jugando(enter): ")
                    
                    if desicion == "1":
                        
                        # Terminar proceso de DESCARTE con la CARTA_CORTE
                        descartar(carta, descarte, jugador, jugadores)
                        
                        # Iniciar Proceso de Corte                        
                        cortar(jugador, jugadores)
                
                proceso_descartar(jugador, jugadores, descarte)
    
    # FIN DEL JUEGO
    print("\n************** COMIENZO DE JUEGO **************\n")
          
            
                
            
        
