import random
def jugadas():
    jugadaUsuario = input("Ingresar Jugada: Piedra(pi), Papel(pa) o Tijeras(ti): ").lower()
    jugadaComputadora = random.choice(['pi','pa','ti'])
    def ganoUsuario(u,c):
        #cuando gana el usuario:
        #usuario: piedra computadora: tijera
        #usuario: tijera computadora: papel
        #usuario: papel computadora: piedra

        if ((u=='pi' and c == 'ti')
            or ( u=='ti' and c == 'pa')
            or (u=='pa' and c == 'pi')):
            return True
        else:
            return False

    if(jugadaUsuario==jugadaComputadora):
        return 'Empate!!!'
    
    
    if ganoUsuario(jugadaUsuario,jugadaComputadora):
        print("Ganaste!!!\n")
        print("tu jugada:", jugadaUsuario)
        print("\nJugada de la Computadora:", jugadaComputadora)

    

    return "Perdiste!!!"
   


    


print(jugadas())


