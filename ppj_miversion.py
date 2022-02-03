import random

#mostramos un cartel en pantalla

print("*********** PIEDRA, PAPEL O TIJERAS!!! ***********")
print("Para comenzar a jugar debes ingresar Piedra(pi), Papel(pa) o Tijeras(ti)")
#jugada del usuario
jugadaUsuario = input("Tu jugada: ").lower()
#jugada de la computadora
jugadaComputadora = random.choice(['pi','pa','ti'])
def mostrarJugadas():
    print("Tu Jugada:", jugadaUsuario)
    print("Jugada de Computadora:", jugadaComputadora)

#definimos si hay empate porque ambos jugaron iguales
if (jugadaUsuario == jugadaComputadora):
    print("Empate")
    mostrarJugadas()
#definimos si ganó el usuario
#el usuario gana cuando se cumpla alguna de estas condiciones:
#usuario = pi computadora = ti
#usuario = ti computadora = pa
#usuario = pa computadora = pi

if (
    (jugadaUsuario == 'pi' and jugadaComputadora== 'ti')or
    (jugadaUsuario == 'ti' and jugadaComputadora == 'pa')or
    (jugadaUsuario == 'pa' and jugadaComputadora == 'pi')
    ):
    print("Ganaste!!!")
    mostrarJugadas()
else:
    print("Perdiste!!!")
    mostrarJugadas()


