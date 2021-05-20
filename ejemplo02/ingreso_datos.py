from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#se lee el archivo datos_clubs.txt
#guardamos en tokens los datos de cada club
#y se guardan los datos de cada club en la tabla Club de la BD
#y se cierra la lectura del archivo datos_clubs.txt
archivo = open('data/datos_clubs.txt', 'r', encoding='utf-8')
for linea in archivo:
    linea = linea.replace('\n', '')
    token = linea.split(';')
    #print(token)
    club = Club(nombre=token[0], deporte=token[1], fundacion=token[2])
    session.add(club)
archivo.close()

#se lee el archivo datos_jugadores.txt
#guardamos en tokens los datos de cada jugador
#se hace una consulta para saber el club al cual pertenece cada jugador
#y se guardan los datos de cada jugador en la tabla jugador de la BD
#y se cierra la lectura del archivo datos_jugadores.txt
archivo = open('data/datos_jugadores.txt', 'r', encoding='utf-8')
for linea in archivo:
    linea = linea.replace('\n', '')
    token = linea.split(';')
    consultaClub = session.query(Club).filter_by(nombre=token[0]).one()
    #print(token)
    #print(consultaClub)
    jugador = Jugador(nombre=token[3], dorsal=token[2], posicion=token[1], club=consultaClub)
    session.add(jugador)
archivo.close()

# se confirma las transacciones
session.commit()